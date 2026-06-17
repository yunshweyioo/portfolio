#!/usr/bin/env python3
"""Dev server for the portfolio: no-cache + live-reload injection.

Serves the static files but (a) disables caching so the preview always
fetches the latest bytes and (b) injects a tiny polling script into HTML
responses that reloads the page whenever a watched file changes on disk.
The injection happens only in the served response — the source HTML file
on disk is never modified.
"""
import http.server
import os
import sys

WATCH = "yun_oo_portfolio.html"

RELOAD_SNIPPET = b"""
<script>
(function () {
  var last = null;
  setInterval(function () {
    fetch('/__mtime', { cache: 'no-store' })
      .then(function (r) { return r.text(); })
      .then(function (t) {
        if (last === null) { last = t; return; }
        if (t !== last) { location.reload(); }
      })
      .catch(function () {});
  }, 1000);
})();
</script>
"""


class Handler(http.server.SimpleHTTPRequestHandler):
    def _no_cache(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

    def do_GET(self):
        # serve the portfolio at the root so the preview panel (which loads "/")
        # shows it directly instead of a directory listing
        if self.path.split("?")[0] in ("/", ""):
            self.path = "/" + WATCH

        # mtime endpoint used by the live-reload poller
        if self.path.split("?")[0] == "/__mtime":
            try:
                mtime = str(os.path.getmtime(WATCH))
            except OSError:
                mtime = "0"
            body = mtime.encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self._no_cache()
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        # inject the reload snippet into HTML files
        path = self.translate_path(self.path)
        if path.endswith(".html") and os.path.isfile(path):
            with open(path, "rb") as f:
                body = f.read()
            if b"</body>" in body:
                body = body.replace(b"</body>", RELOAD_SNIPPET + b"</body>", 1)
            else:
                body += RELOAD_SNIPPET
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self._no_cache()
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        super().do_GET()

    def end_headers(self):
        # belt-and-suspenders: no-cache on any other asset too
        self._no_cache()
        super().end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4599
    http.server.HTTPServer(("127.0.0.1", port), Handler).serve_forever()

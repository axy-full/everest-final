#!/usr/bin/env python3
"""Local dev server with Vercel-style clean URLs (/films -> films.html) and no caching."""
import http.server
import os

PORT = 4552
ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def translate_path(self, path):
        p = super().translate_path(path)
        bare = path.split('?')[0].split('#')[0]
        if not os.path.exists(p) and not bare.endswith('/') and '.' not in os.path.basename(bare):
            candidate = p + '.html'
            if os.path.exists(candidate):
                return candidate
        return p

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

    def log_message(self, *args):
        pass


if __name__ == '__main__':
    with http.server.ThreadingHTTPServer(('127.0.0.1', PORT), Handler) as srv:
        print(f'Serving Everest Final Version at http://localhost:{PORT}')
        srv.serve_forever()

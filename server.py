"""
CollabPromo.com - Local Development & Demonstration Server
Zero-dependency Python 3 standard library server.
Serves static assets with ES module MIME types and provides REST API endpoints.
"""

import sys
import os
import json
import mimetypes
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

# Ensure proper MIME types for ES modules and styles
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("text/html", ".html")
mimetypes.add_type("application/json", ".json")

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CollabPromoRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and disable caching for seamless local testing
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        
        # REST API endpoints
        if parsed.path == "/api/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "status": "healthy",
                "service": "CollabPromo.com",
                "version": "1.0.0",
                "description": "Mediated Creator-Brand Promotional Matching Platform"
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return

        # SPA Fallback: If requested path doesn't exist on disk, serve index.html
        path_on_disk = os.path.join(DIRECTORY, parsed.path.lstrip("/"))
        if not os.path.exists(path_on_disk) and not parsed.path.startswith("/api/"):
            self.path = "/index.html"

        # Default static file handling
        return super().do_GET()


def run_server(host="0.0.0.0", port=PORT):
    server_address = (host, port)
    try:
        httpd = HTTPServer(server_address, CollabPromoRequestHandler)
        print(f"============================================================")
        print(f" CollabPromo.com Local Server Running")
        print(f" Local URL: http://localhost:{port} or http://127.0.0.1:{port}")
        print(f" Serving Directory: {DIRECTORY}")
        print(f" Press Ctrl+C to stop the server.")
        print(f"============================================================")
        httpd.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"Port {port} is in use. Trying port {port + 1}...")
            run_server(host, port + 1)
        else:
            raise e
    except KeyboardInterrupt:
        print("\nCollabPromo server stopped.")
        sys.exit(0)

if __name__ == "__main__":
    port_arg = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    run_server("0.0.0.0", port_arg)

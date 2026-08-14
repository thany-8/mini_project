#!/usr/bin/env python3
"""file.py — Serve this project folder locally and open the flyer in your browser.

Usage:
    python3 file.py             # serve on http://localhost:8000 and open the flyer
    python3 file.py 9000        # use a custom port
    python3 file.py --no-open   # just serve, don't open the browser

Press Ctrl+C to stop the server.
"""
from __future__ import annotations

import argparse
import http.server
import os
import socket
import socketserver
import threading
import webbrowser

DEFAULT_PORT = 8000
FLYER = "flyer-review.html"


def find_free_port(preferred: int) -> int:
    """Return `preferred` if it's free, otherwise the next available port."""
    for port in range(preferred, preferred + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex(("127.0.0.1", port)) != 0:
                return port
    return preferred


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Serve this folder over HTTP and open the flyer."
    )
    parser.add_argument(
        "port", nargs="?", type=int, default=DEFAULT_PORT,
        help=f"Port to serve on (default: {DEFAULT_PORT}).",
    )
    parser.add_argument(
        "--no-open", action="store_true",
        help="Do not open the browser automatically.",
    )
    args = parser.parse_args()

    # Serve the folder this script lives in, so it works no matter where it's run from.
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    port = find_free_port(args.port)
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
        base = f"http://localhost:{port}"
        target = f"{base}/{FLYER}" if os.path.exists(FLYER) else base
        print(f"Serving {root}")
        print(f"  -> {target}")
        print("Press Ctrl+C to stop.")

        if not args.no_open:
            threading.Timer(0.5, webbrowser.open, args=(target,)).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server...")
        finally:
            httpd.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

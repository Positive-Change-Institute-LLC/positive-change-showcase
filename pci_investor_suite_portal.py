#!/usr/bin/env python3
"""Serve a generated investor portfolio browser on loopback only."""

from __future__ import annotations

import argparse
import functools
import http.server
import sys
import webbrowser
from pathlib import Path

DEFAULT_PORTFOLIO = Path("PCI_Python_Portfolio_Full")
DEFAULT_PORT = 8765


class LocalPortfolioHandler(http.server.SimpleHTTPRequestHandler):
    server_version = "PCIInvestorSuite/1.0"

    def translate_path(self, path: str) -> str:
        translated = Path(super().translate_path(path))
        root = Path(self.directory).resolve()
        if _has_symlink_component(translated):
            return str(root / "__not_found__")
        try:
            translated.resolve().relative_to(root)
        except (OSError, ValueError):
            return str(root / "__not_found__")
        return str(translated)

    def end_headers(self) -> None:
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; img-src 'self' data:; media-src 'self'; "
            "style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; "
            "object-src 'none'; base-uri 'none'; frame-ancestors 'none'",
        )
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def serve(portfolio_dir: Path, port: int = DEFAULT_PORT, open_browser: bool = False) -> None:
    portfolio_path = portfolio_dir.expanduser().absolute()
    if _has_symlink_component(portfolio_path):
        raise ValueError("Portfolio path must not pass through a symbolic link.")
    root = portfolio_path.resolve()
    if not root.is_dir():
        raise ValueError(f"Portfolio directory not found: {root}")
    index_path = root / "portfolio_index.json"
    dashboard_path = root / "investor_dashboard.html"
    if index_path.is_symlink() or not index_path.is_file():
        raise ValueError(
            "No portfolio_index.json found. Run pci_portfolio_master_builder_v2.py --build first."
        )
    if dashboard_path.is_symlink() or not dashboard_path.is_file():
        raise ValueError(
            "No investor_dashboard.html found. Rebuild the portfolio with the current builder."
        )

    handler = functools.partial(LocalPortfolioHandler, directory=str(root))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    url = f"http://127.0.0.1:{port}/investor_dashboard.html"
    print(f"Local investor portal: {url}")
    print("Bound to 127.0.0.1 only. Press Ctrl+C to stop.")
    if open_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nInvestor portal stopped.")
    finally:
        server.server_close()


def _has_symlink_component(path: Path) -> bool:
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current /= part
        if current.is_symlink():
            return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--portfolio-dir", type=Path, default=DEFAULT_PORTFOLIO)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--open", action="store_true", help="Open the local portal in the default browser.")
    args = parser.parse_args(argv)
    if not 1024 <= args.port <= 65535:
        parser.error("--port must be between 1024 and 65535.")
    try:
        serve(args.portfolio_dir, args.port, args.open)
    except (OSError, ValueError) as exc:
        print(f"[PCIInvestorSuite] Stopped: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

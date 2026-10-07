"""Local demonstration API for the PCI enterprise QR dashboard.

This demo does not connect wallets, submit transactions, or retain analytics.
"""

from __future__ import annotations

import re
from pathlib import Path

import qrcode
from flask import Flask, jsonify, request, send_file

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
FRONTEND = PACKAGE_ROOT / "frontend" / "index.html"
PRODUCT_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,80}$")
WALLET_PROVIDERS = {"Base", "Coinbase", "Phantom", "Trust"}
ALLOWED_ACTIONS = {"view", "purchase", "transfer"}
ALLOWED_EVENTS = {"dashboard_opened", "metadata_viewed", "qr_generated", "action_simulated"}

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024


def valid_product_id(value: object) -> bool:
    return isinstance(value, str) and PRODUCT_ID_PATTERN.fullmatch(value) is not None


@app.get("/")
def index():
    return send_file(FRONTEND)


@app.get("/api/product_metadata")
def product_metadata():
    wallet = request.args.get("wallet", "")
    product_id = request.args.get("product_id", "")
    if not isinstance(wallet, str) or wallet not in WALLET_PROVIDERS:
        return jsonify(error="wallet must be one of the supported provider names"), 400
    if not valid_product_id(product_id):
        return jsonify(error="product_id must be 1-80 letters, numbers, underscores, or hyphens"), 400

    return jsonify(
        wallet_provider=wallet,
        product_id=product_id,
        narration_trigger="not_configured",
        lidar_effect=False,
        elemental_motifs=["⚙️", "🔮", "🧠", "⚡️", "📈", "🩻"],
        compliance="Made in USA — Positive Change Institute LLC",
        status="demo_metadata",
    )


@app.get("/api/qr")
def qr_code():
    product_id = request.args.get("product_id", "")
    if not valid_product_id(product_id):
        return jsonify(error="product_id must be 1-80 letters, numbers, underscores, or hyphens"), 400

    code = qrcode.QRCode(border=2, box_size=1)
    code.add_data(f"pci-product:{product_id}")
    code.make(fit=True)
    matrix = code.get_matrix()
    size = len(matrix)
    modules = " ".join(
        f"{column},{row}"
        for row, line in enumerate(matrix)
        for column, dark in enumerate(line)
        if dark
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" '
        f'role="img" aria-label="QR code for product {product_id}">'
        f'<rect width="{size}" height="{size}" fill="white"/>'
        f'<path fill="#10131d" d="'
        + "".join(f"M{x} {y}h1v1h-1z" for x, y in (map(int, item.split(",")) for item in modules.split()))
        + '"/></svg>'
    )
    return app.response_class(svg, mimetype="image/svg+xml")


@app.post("/api/transaction")
def transaction():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="request body must be a JSON object"), 400
    wallet = data.get("wallet")
    action = data.get("action")
    product_id = data.get("product_id")
    if not isinstance(wallet, str) or wallet not in WALLET_PROVIDERS:
        return jsonify(error="wallet must be one of the supported provider names"), 400
    if not isinstance(action, str) or action not in ALLOWED_ACTIONS:
        return jsonify(error="action must be view, purchase, or transfer"), 400
    if not valid_product_id(product_id):
        return jsonify(error="product_id must be 1-80 letters, numbers, underscores, or hyphens"), 400

    return jsonify(
        status="simulation_only",
        submitted=False,
        tx_hash=None,
        wallet_provider=wallet,
        product_id=product_id,
        action=action,
        message="No wallet was connected and no blockchain transaction was submitted.",
    )


@app.post("/api/analytics")
def analytics():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="request body must be a JSON object"), 400
    event = data.get("event")
    product_id = data.get("product_id")
    if not isinstance(event, str) or event not in ALLOWED_EVENTS:
        return jsonify(error="event is not supported"), 400
    if product_id is not None and not valid_product_id(product_id):
        return jsonify(error="product_id is invalid"), 400
    return jsonify(status="received", retained=False)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

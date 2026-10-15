# Copilot Walkthrough — Enterprise PDF Dossier

1. Treat the supplied FPDF script as a proposal; do not run it or import it as repository code.
2. Verify the product-count claim against the actual list: it contains three sample entries and a placeholder comment, not 150+ complete products.
3. Do not copy its hard-coded contact email into source, docs, fixtures, PDFs, or QR payloads without explicit approval.
4. Verify each product claim, price, and destination against an approved source. A generated PDF or QR code does not verify a patent, payment rail, storefront, or product.
5. If implementing later, declare dependencies through the project package process, move generation behind an explicit entrypoint, and write to a caller-selected output path.
6. Test missing fields, unsupported characters, image/font behavior, PDF output, and decoded QR contents using non-sensitive fixture data.
7. Keep generated dossiers and private contact information out of the public Pages artifact unless reviewed for publication.

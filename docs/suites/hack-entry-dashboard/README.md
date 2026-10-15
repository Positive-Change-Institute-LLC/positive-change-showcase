# HackEntry Cinematic Dashboard Proposal

## Status

The supplied “Hack Entry: Positive Change Institute LLC” generator is not checked-in application code. Its PDF, JSON, QR, and HTML outputs are not evidence of a real hackathon submission, product integration, wallet, NFT collection, or live dashboard.

The wallet and product records are synthetic: wallet names are `Wallet_1` through `Wallet_12`, product labels are `Product_1` through `Product_150`, and token balances and rarity labels are randomly generated. They do not come from users, the product catalog, a chain, or an NFT contract. The QR destination and the PDF's claims about 150+ integrated turnkeys are unverified.

## Implementation gaps

- The page starts an asynchronous fetch for wallet data and immediately builds its Lidar nodes from the still-empty `wallets` object. The draw loop therefore starts with no nodes or flows.
- Epic/Mythic highlighting searches the synthetic product labels for rarity names, so it does not reflect the separately generated rarity arrays.
- Product overlay values are random chart data, not product or wallet analytics.
- Audio files are referenced but not supplied. The generator also depends on `reportlab` and `qrcode`, which are not declared for this proposal.
- The generated QR code and PDF are written to a local output directory; no verified hosted dashboard or integration is established.

## Safe handling

Do not publish its generated PDF or QR as proof of live functionality. Use a temporary output directory for any reviewed experiment, label all generated values as synthetic, validate the destination before creating a public QR code, and keep user wallet data and credentials out of fixtures and public artifacts.

Any future dashboard that consumes external product or wallet data must validate the data contract and safely render user-controlled values. The supplied overlay and tooltip use `innerHTML`, which is unsafe if the current hard-coded labels are replaced by untrusted data.

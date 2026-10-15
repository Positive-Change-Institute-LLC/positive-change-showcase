# BlueChip Turnkey Launch-Kit Generator

This repository includes a **one-shot local generator** for the Genesis Relics launch-kit concept. It copies any supplied concept art, creates labeled social graphics, and writes a fresh PowerPoint deck. Each run replaces the deck instead of appending duplicate slides.

## Run

Install the pinned dependencies, then run from the repository root:

```sh
python -m pip install -r bluechip_launch_requirements.txt
python BlueChip_Turnkeys_AutoQueue.py \
  --source-dir /path/to/concept-art \
  --output-dir /path/to/launch-kits
```

The source directory may omit either render; missing art is reported, promo art for it is skipped, and the deck still contains a clear placeholder. Outputs are written only when the command runs.

## Important limitations

- This is not a background service and does not poll or start a thread. Run it manually when you want to regenerate the local files.
- The supplied prices are labeled as proposed prices, not active offers, appraisal, guaranteed value, or investment advice. Verify pricing, benefits, and terms before publication.
- Payment links in the supplied sample were placeholders or unverified, so this generator deliberately creates no payment QR codes and does not process payments.
- The workflow does not connect to AI services, wallets, NFT contracts, marketplaces, or storefronts. Narration copy and art overlays are static local outputs.
- Generated launch-kit files are not automatically published, and adding concept art does not establish copyright or trademark ownership.

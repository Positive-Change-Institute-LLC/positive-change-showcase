# Copilot Walkthrough — Public Homepage

1. Read the root `index.html`, root README, and Pages workflow before changing navigation or publication.
2. Test relative links against the `_site` paths, not only repository paths.
3. Use product names exactly as listed in the maintained catalog; do not add a purchase/status claim unless the target is verified.
4. Keep external links safe (`target="_blank"` requires `rel="noopener noreferrer"`).
5. Do not add secrets, credentials, fake login, or transaction success messages to static HTML.
6. For each new linked asset, update `.github/workflows/deploy.yml` and verify the artifact includes it.

# Copilot Walkthrough — PCI Automation Suite

1. Treat the conversation snippet as a design proposal; it is not currently a repository file.
2. Before implementing it, inspect the existing product catalogs, deployment suite, and generated portfolio tools to avoid creating parallel registries.
3. Use exact source names when reconciling catalog rows, such as **Prometheus Sovereign Intelligence** or **Investor Dashboard**; preserve provenance when similarly named entries differ.
4. Validate registry IDs, included product references, output paths, and encoding before writing generated files.
5. Keep generators idempotent and write only into an explicit output directory; test that dry-run has no side effects and existing files are not overwritten silently.
6. Do not treat embedded Whop IDs, marketing descriptions, or links as live provider data.
7. Keep external deployment behind the existing manifest-driven, dry-run-first orchestrator rather than introducing inline deployment commands.

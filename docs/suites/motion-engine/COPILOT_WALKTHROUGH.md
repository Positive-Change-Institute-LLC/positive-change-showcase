# Copilot Walkthrough — Motion Engine

1. Read the motion engine's `SURFACE_PROFILES`, engine stubs, and the existing dashboard CSS animation/reduced-motion behavior.
2. Preserve explicit surface selection and deterministic profile output; document new surfaces and profiles.
3. Do not call print stubs "rendering" or "deployment". Connect a renderer only through an explicit, tested interface.
4. Keep motion optional and honor `prefers-reduced-motion`; avoid high-frequency or flashing effects.
5. If connecting the 333 FX catalog, define and validate a data contract first. Current files have no such integration.
6. Run the script and inspect the printed profile list after profile changes; add tests for selection and enabled cycles before claiming interoperability.
7. Do not describe the supplied telemetry, AI self-optimization, or automatic animation claims as active behavior; the checked-in implementation has print-only engine and cycle stubs.

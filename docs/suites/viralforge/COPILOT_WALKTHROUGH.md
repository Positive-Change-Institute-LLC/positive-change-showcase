# Copilot Walkthrough — ViralForge™ Pro

1. Treat the ViralForge™ Pro catalog entry as an asset listing, not evidence that application source or a deployed service exists in this repository.
2. Do not copy the supplied page into a public frontend or add a real Claude/Anthropic key. The proposed browser flow exposes the user's key to the client runtime and request tools.
3. Keep provider credentials server-side behind an authenticated, rate-limited backend; never put them in HTML, JavaScript, browser storage, or public Pages artifacts.
4. Before any model-backed renderer is used, validate the response shape and safely render every untrusted field. Do not interpolate model output into `innerHTML`.
5. Separate deterministic demo fixtures from provider-backed output. Remove unsupported income, viral-score, platform-count, and “live AI” assertions or label them as unverified examples.
6. Implement regeneration, enhancement, publishing, and analytics only when real interfaces exist; a notification or static mock is not an integration.
7. Test empty topics, unsupported platform values, malformed provider responses, provider failures, and HTML-like content without sending a real key or publishing posts.

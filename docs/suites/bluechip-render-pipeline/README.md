# BlueChip Turnkey Render and Publish Pipeline Proposal

## Status

The supplied scripts are proposals, not a checked-in or deployable pipeline. The repository does not contain the proposed queue state, turnkey release trees, narration or motif tools, renderer containers, signing key, AWS configuration, NAS/backup mounts, or Whop/Linktree integrations. No media has been rendered or published.

The variants also differ in behavior: one invokes separate TTS and motif generators, while another only passes narrator and motif values to a container. The promo/deck scripts generate graphics and presentation content only when source images and dependencies are present; their background loop repeatedly reprocesses the queue.

## Safety and correctness boundaries

- Do not run the supplied scripts. They perform work at import/top level, have no dry-run or confirmation gate, and combine local file writes with cloud upload and Git publication.
- `hard_copy()` recursively deletes an existing destination before copying. Queue names and manifest paths are not constrained to an approved root, and the code does not protect reviewed releases from replacement.
- The scripts load a private key from a local path and automatically upload files and push commits/tags. Never add private keys or credentials to the repository. External publishing must not occur without separate review and explicit operator confirmation.
- The integrity check compares a file's hash to a value computed from that same file during the run; it does not compare against an independently trusted manifest value. The signature is not verified, and it does not establish legal ownership or protection.
- The “Whop” and “Linktree” steps print constructed links; they do not call provider APIs. The S3 hostname, payment URLs, prices, and membership tiers are not verified or approved.
- Names of real performers are not authorization to synthesize or imitate their voices. Use original, properly licensed narration with documented permissions. Confirm rights for all imagery, fonts, music, and other assets.
- Randomly changing prices and presenting sample benefits as current offers could mislead customers. Only publish owner-approved, accurate catalog data.

The repository already has a separate [dry-run-first deployment orchestrator](../deployment/README.md). Any future pipeline should keep rendering local and deterministic first, validate inputs and outputs, avoid destructive overwrite behavior, and leave external upload or Git publication behind reviewed deployment configuration.

## Safe next steps

Before implementation, define the approved queue/manifest schema, asset sources and rights, supported narrator provider, output directory, versioning, and expected hash/signature verification procedure. Add tests for malformed manifests, unsafe paths, missing assets, existing release destinations, and failed external operations. Keep credentials in an approved runtime secret store and keep publishing disabled by default.

# 🩺 Repository Health and Navigation Diagnostic

**Snapshot:** 2026-10-15 (UTC)  
**Scope:** `Positive-Change-Institute-LLC/positive-change-showcase` and its visible GitHub Actions runs. This is not an audit of the user's other repositories, GitHub account settings, branch protections, secrets, or billing.

## 🧭 Quick links

- [Alphabetical suite directory](suites/README.md)
- [Integration guide](INTEGRATION_GUIDE.md)
- [GitHub Actions overview](https://github.com/Positive-Change-Institute-LLC/positive-change-showcase/actions)
- [CI workflow runs](https://github.com/Positive-Change-Institute-LLC/positive-change-showcase/actions/workflows/ci.yml)
- [Pages deployment runs](https://github.com/Positive-Change-Institute-LLC/positive-change-showcase/actions/workflows/deploy.yml)
- [AI pull request review runs](https://github.com/Positive-Change-Institute-LLC/positive-change-showcase/actions/workflows/pr-review.yml)

## 🕰️ Chronological Actions timeline

| Date (UTC) | Workflow / event | Observed health |
|---|---|---|
| 2026-08-27 | [GitHub Pages workflow](https://github.com/Positive-Change-Institute-LLC/positive-change-showcase/actions/workflows/deploy.yml) registered | Active workflow. Its latest visible run in this audit is the failed 2026-10-08 run below. |
| 2026-10-04 | [CI workflow](https://github.com/Positive-Change-Institute-LLC/positive-change-showcase/actions/workflows/ci.yml) registered; [latest pre-audit CI run](https://github.com/Positive-Change-Institute-LLC/positive-change-showcase/actions/runs/37211139447) | Run succeeded, but no later CI run appeared in the Actions history reviewed. The `ci.yml` file was absent from the default branch; this working branch now adds its source and standard-library unit-test command. It must be merged before the default-branch push trigger can verify it. |
| 2026-10-07 | [AI pull request review workflow](https://github.com/Positive-Change-Institute-LLC/positive-change-showcase/actions/workflows/pr-review.yml) registered | Active workflow. |
| 2026-10-08 18:42 | [Pages run #10](https://github.com/Positive-Change-Institute-LLC/positive-change-showcase/actions/runs/37826385258) | **Failed:** `actions/configure-pages` reported “Parameter token or opts.auth is required.” The run used the default-branch workflow, which passed only `secrets.PAGES_TOKEN`. The current working branch has a `github.token` fallback, but default branch has not yet been verified with a new run. |
| 2026-10-08 18:47 | [AI review run #30](https://github.com/Positive-Change-Institute-LLC/positive-change-showcase/actions/runs/37788160528) | **Failed:** GitHub Models returned the plain text `OK`; the inference action then errored while expecting a structured response. A later review run succeeded. |
| 2026-10-15 10:46 | [AI review run #33](https://github.com/Positive-Change-Institute-LLC/positive-change-showcase/actions/runs/38722596657) | **Succeeded:** all review job steps completed. This is the latest direct project workflow run found in the audit. |

GitHub's workflow registry also showed two Copilot-managed workflows. They are platform workflows and are not counted as project test/deployment checks here. Action status is time-sensitive; use the linked live run pages for current results.

## 🔎 Findings and next actions

| Priority | Finding | Recommended follow-up |
|---|---|---|
| High | The latest recorded Pages deployment failed because the token was missing. The current checkout has `${{ secrets.PAGES_TOKEN || github.token }}`, while the default branch copy still used only `${{ secrets.PAGES_TOKEN }}` when checked. | Merge the fallback change, then run Pages from the default branch and confirm site setup/deployment. |
| High | The Pages build copies every root-level `*.csv` and `*.json` file into the public artifact. New files matching those globs are published automatically. | Review the files intended for public release and prefer an explicit asset list over broad globs. |
| Medium | Actions' last existing CI success is from 2026-10-04, before this working branch adds `.github/workflows/ci.yml`. The default branch still needs this change merged. | Merge the workflow, then confirm its first default-branch push run succeeds; keep the workflow source checked in for future pull requests. |
| Medium | No CI run has yet validated the current source snapshot. | After merge, confirm the new workflow executes `python3 -m unittest discover -s tests -v`. |

## ✅ Local checks

- `python -m unittest discover -s tests -v` — **21 tests passed** on the audited checkout.
- The passing tests confirm working behavior in the covered components. Capability-boundary findings above identify what is not implemented or verified; they are not a declaration that existing Intelligence code is nonfunctional.
- The new CI workflow uses the same test discovery command with `python3`.
- Suite index links and repository Markdown links should be checked whenever navigation changes; the suite index now has a single alphabetically sorted directory.
- The deployment orchestrator is separate from Pages and remains dry-run by default; production execution requires explicit confirmation. See the [deployment guide](suites/deployment/README.md).
- Corrected the root README's Whop badge to say its links are unverified, matching the documented absence of a live Whop integration.

## Scope note

“Defrag” here means improving discoverability without moving source files or changing import/deployment paths. This report cannot change settings or files in other GitHub repositories. The linked live Actions pages are authoritative for any run started after this snapshot.

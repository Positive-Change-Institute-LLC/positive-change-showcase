# Copilot Walkthrough — Bootstrap Utilities

1. Read all three bootstrap scripts before editing templates or file ownership rules.
2. Start with `--help` and `--dry-run`; inspect the summarized target paths before any write.
3. Preserve repository-root validation, safe managed-file behavior, and explicit `--force` overwrite semantics.
4. Use exact existing product names, for example **AI Business Builder**, only as human-readable template metadata. Never infer a product API or create an undocumented offering.
5. Test dry-run creates no files, normal mode preserves existing managed content, and `--force` changes only the intended paths.
6. Keep generated output out of commits unless the task explicitly asks for the scaffold and its contents.
7. Do not include API keys, wallet secrets, or production config in generated templates.

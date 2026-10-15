# Bootstrap Utilities

These utilities create repository scaffolding; they do not deploy generated code or register products.

| Script | Purpose |
|---|---|
| `bootstrap_pswe_repo.py` | Creates a lightweight showcase scaffold, optionally reporting changes as JSON |
| `bootstrap_ppci_sws.py` | Scaffolds the Prometheus × PCI sovereign wealth stack |
| `bootstrap_signal_layers.py` | Writes `core/signals.py` from supplied or default signal labels |

All accept a `--repo-root` target. Review each script's `--help` output before execution. Use `--dry-run` first; only use `--force` after checking which existing files may be overwritten.

Example with a real catalog product name:

```bash
python bootstrap_pswe_repo.py --project-name "AI Business Builder" --repo-root /tmp/pci-showcase-review --dry-run
```

The name supplies template metadata only; it does not connect that catalog product to the scaffold. Do not put secrets in generated files or commands.

## Interoperability

The stack bootstrap can create structures used by `ppci_sws_proof`; the signal bootstrap creates an independent module. No bootstrap utility configures QuickNode, Circle, Whop, Shopify, credentials, or live deployment targets.

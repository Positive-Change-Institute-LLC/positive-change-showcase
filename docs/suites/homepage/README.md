# PCI Public Homepage

The root `index.html` is a static landing page with links to public surfaces, including the Prometheus Command Dashboard and the Arcana concept showcase. It does not implement product checkout or account services.

## Local preview

From the repository root:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. GitHub Pages publication is handled separately by `.github/workflows/deploy.yml`, which copies a specific set of files and directories to `_site`.

Catalog names such as **Resilience OS Toolkit** and **Investor Dashboard** are not proof of a live purchase path. Outbound links are links only.

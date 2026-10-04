# prometheus_core

Reference implementations of the Prometheus engines. Standard library only; no network access, trading, or key handling.

| Module | Engine | What it does |
|---|---|---|
| `memory.py` | Memory System | Persistent JSON store with search by text, kind and tag |
| `synthesizer.py` | Synthesizer | Fuses multi-source claims into ranked findings (noisy-OR confidence) |
| `evolution.py` | Evolution Engine | Compares metrics to targets, flags weaknesses, recommends actions |
| `content.py` | AI Content Engine | Deterministic template-driven articles, posts and product copy with brand checks (no external AI calls) |
| `legacy.py` | Digital Legacy System | SHA-256 manifest of assets; verifies missing, modified or added files |
| `development.py` | Personal Development System | Habit streaks and goal progress with JSON persistence |
| `pswe.py` | Sovereign Wealth Engine | Dollar-cost-averaging simulator over a price series (educational, not financial advice) |

## Quick start
```python
from prometheus_core import MemorySystem, Synthesizer, EvolutionEngine, simulate_dca

mem = MemorySystem("memory.json")
mem.add("lesson", "Keep long-term holdings in cold storage", tags=["security"])

syn = Synthesizer()
syn.observe("report-a", "Demand is rising", 0.5)
syn.observe("report-b", "Demand is rising", 0.5)
print(syn.synthesize()[0])          # confidence 0.75

print(EvolutionEngine({"tests": 10}).review({"tests": 4})[0].recommendation)
print(simulate_dca([10, 20], 100).return_pct)   # 50.0
```

## Run everything
```bash
python -m prometheus_core
```

## Tests
```bash
pip install pytest
python -m pytest tests -q
```

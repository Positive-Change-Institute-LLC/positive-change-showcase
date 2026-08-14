# core/yield_analysis.py — Yield Decomposition Analysis


def analyze_yield(protocol):
    real = protocol.get("real_yield", 0.03)
    emissions = protocol.get("emissions", 0.02)
    synthetic = protocol.get("synthetic", 0.01)

    return {
        "real_yield": real,
        "emissions": emissions,
        "synthetic_yield": synthetic,
        "yield_quality": "high" if real > emissions else "medium",
    }

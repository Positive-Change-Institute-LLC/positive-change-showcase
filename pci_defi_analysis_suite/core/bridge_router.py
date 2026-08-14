# core/bridge_router.py — Bridge & Router Analysis


def analyze_bridge(bridge):
    finality = bridge.get("finality", 300)
    trust = bridge.get("trust", "optimistic")

    return {
        "finality_seconds": finality,
        "trust_model": trust,
        "oracle_risk": "high" if trust == "trusted" else "medium",
    }

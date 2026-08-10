# utils/scoring.py — PCI Resilience Scoring


def score_resilience(structure):
    score = 0
    if structure.get("invariant_stability") == "high":
        score += 30
    if structure.get("volatility_exposure") == "low":
        score += 20
    if structure.get("liquidity_depth") == "high":
        score += 30
    if structure.get("oracle_risk") == "low":
        score += 20
    return min(score, 100)

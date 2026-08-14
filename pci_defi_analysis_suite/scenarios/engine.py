# scenarios/engine.py — Stress Scenario Simulation Engine


def simulate_volatility(structure):
    return {
        "shock": "volatility",
        "impact": "high" if structure["volatility_exposure"] == "high" else "medium",
    }


def simulate_liquidity(structure):
    return {
        "shock": "liquidity_withdrawal",
        "impact": "high" if structure["liquidity_depth"] == "low" else "medium",
    }


def simulate_oracle_failure(structure):
    return {
        "shock": "oracle_failure",
        "impact": "critical" if structure["oracle_risk"] == "high" else "medium",
    }


def simulate_governance_change(structure):
    return {"shock": "governance_change", "impact": "low"}


def simulate_fee_shift(structure):
    return {"shock": "fee_shift", "impact": "medium"}

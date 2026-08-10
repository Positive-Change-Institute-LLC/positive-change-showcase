# core/lending_analysis.py — Lending Market Structural Analysis


def analyze_lending(market):
    utilization = market["borrowed"] / market["supplied"]
    collateral_factor = market.get("collateral_factor", 0.75)

    liquidation_risk = (
        "high" if utilization > 0.8 else
        "medium" if utilization > 0.5 else
        "low"
    )

    return {
        "utilization": utilization,
        "collateral_factor": collateral_factor,
        "liquidation_risk": liquidation_risk,
        "oracle_risk": "medium",
    }

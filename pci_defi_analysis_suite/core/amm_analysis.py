# core/amm_analysis.py — AMM Structural Analysis
from pci_defi_analysis_suite.utils.math import invariant_xyk, price_impact


def analyze_amm(pool):
    x = pool["reserve0"]
    y = pool["reserve1"]
    fee = pool.get("fee", 0.003)

    invariant = invariant_xyk(x, y)
    impact_small = price_impact(100, x, y)
    impact_large = price_impact(10000, x, y)

    return {
        "curve": "xyk",
        "invariant": invariant,
        "fee": fee,
        "invariant_stability": "high" if invariant > 1_000_000 else "medium",
        "price_impact_small": impact_small,
        "price_impact_large": impact_large,
        "volatility_exposure": "medium",
        "liquidity_depth": "high" if x + y > 1_000_000 else "medium",
        "oracle_risk": "medium",
    }

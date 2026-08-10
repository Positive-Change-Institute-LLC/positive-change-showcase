# core/lp_risk.py — LP Position Risk Analysis


def lp_risk(lp):
    volatility = lp.get("volatility", 0.5)
    il = volatility * 0.02
    fee_apr = lp.get("fee_apr", 0.1)

    return {
        "impermanent_loss_estimate": il,
        "fee_apr": fee_apr,
        "volatility_exposure": "high" if volatility > 0.6 else "medium",
    }

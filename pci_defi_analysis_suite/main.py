# main.py — PCI DeFi Analysis Suite Full Runner
import json

from pci_defi_analysis_suite.core.amm_analysis import analyze_amm
from pci_defi_analysis_suite.core.lp_risk import lp_risk
from pci_defi_analysis_suite.core.yield_analysis import analyze_yield
from pci_defi_analysis_suite.core.lending_analysis import analyze_lending
from pci_defi_analysis_suite.core.bridge_router import analyze_bridge
from pci_defi_analysis_suite.core.routing_graph import routing_graph
from pci_defi_analysis_suite.scenarios.engine import (
    simulate_fee_shift,
    simulate_governance_change,
    simulate_liquidity,
    simulate_oracle_failure,
    simulate_volatility,
)
from pci_defi_analysis_suite.utils.scoring import score_resilience


def run_defi_analysis():
    amm = analyze_amm({"reserve0": 500000, "reserve1": 800000, "fee": 0.003})
    lp = lp_risk({"reserve0": 500000, "reserve1": 800000, "volatility": 0.4})
    yld = analyze_yield({"real_yield": 0.05, "emissions": 0.02, "synthetic": 0.01})
    lend = analyze_lending({"borrowed": 300000, "supplied": 800000})
    bridge = analyze_bridge({"finality": 180, "trust": "optimistic"})
    routing = routing_graph(["eth->arb", "arb->base"])

    combined_structure = {
        "volatility_exposure": lp["volatility_exposure"],
        "liquidity_depth": amm["liquidity_depth"],
        "oracle_risk": lend["oracle_risk"],
    }

    scenarios = {
        "volatility": simulate_volatility(combined_structure),
        "liquidity": simulate_liquidity(combined_structure),
        "oracle_failure": simulate_oracle_failure(combined_structure),
        "governance_change": simulate_governance_change(combined_structure),
        "fee_shift": simulate_fee_shift(combined_structure),
    }

    resilience = score_resilience({
        "invariant_stability": amm["invariant_stability"],
        "volatility_exposure": lp["volatility_exposure"],
        "liquidity_depth": amm["liquidity_depth"],
        "oracle_risk": lend["oracle_risk"],
    })

    return {
        "amm": amm,
        "lp": lp,
        "yield": yld,
        "lending": lend,
        "bridge": bridge,
        "routing": routing,
        "scenarios": scenarios,
        "resilience_score": resilience,
    }


if __name__ == "__main__":
    print(json.dumps(run_defi_analysis(), indent=4))

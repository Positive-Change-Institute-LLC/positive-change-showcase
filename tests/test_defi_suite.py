from pci_defi_analysis_suite.core.amm_analysis import analyze_amm
from pci_defi_analysis_suite.main import run_defi_analysis
from pci_defi_analysis_suite.utils.math import invariant_xyk, price_impact
from pci_defi_analysis_suite.utils.scoring import score_resilience


def test_invariant():
    assert invariant_xyk(3, 4) == 12


def test_price_impact_grows_with_size():
    assert price_impact(100, 1000, 1000) < price_impact(10000, 1000, 1000)
    assert 0 < price_impact(100, 1000, 1000) < 1


def test_score_bounds():
    best = {"invariant_stability": "high", "volatility_exposure": "low",
            "liquidity_depth": "high", "oracle_risk": "low"}
    assert score_resilience(best) == 100
    assert score_resilience({}) == 0


def test_amm_analysis():
    out = analyze_amm({"reserve0": 500000, "reserve1": 800000})
    assert out["curve"] == "xyk"
    assert out["liquidity_depth"] == "high"


def test_full_analysis_runs():
    assert run_defi_analysis()

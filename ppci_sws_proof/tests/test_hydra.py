import unittest

from ppci_sws_proof.hydra import simulate_hydra


class HydraSimulationTests(unittest.TestCase):
    def test_corridor_expansion(self):
        conservative = simulate_hydra(100_000, 0.2, 0.0)
        expansion = simulate_hydra(100_000, 0.8, 0.7)

        self.assertGreater(
            expansion["yield_corridor"]["spread_bps"],
            conservative["yield_corridor"]["spread_bps"],
        )

    def test_corridor_compression(self):
        baseline = simulate_hydra(250_000, 0.5, 0.0)
        compression = simulate_hydra(250_000, 0.5, -0.8)

        self.assertLess(
            compression["yield_corridor"]["spread_bps"],
            baseline["yield_corridor"]["spread_bps"],
        )
        self.assertEqual(compression["engine_decision"], "defend")

    def test_signal_driven_adjustments(self):
        negative = simulate_hydra(500_000, 0.7, -0.3)
        positive = simulate_hydra(500_000, 0.7, 0.8)

        self.assertGreater(
            positive["yield_corridor"]["max_pct"], negative["yield_corridor"]["max_pct"]
        )
        self.assertEqual(positive["engine_decision"], "accelerate")
        self.assertNotEqual(positive["risk_band"], "capital_preservation")


if __name__ == "__main__":
    unittest.main()

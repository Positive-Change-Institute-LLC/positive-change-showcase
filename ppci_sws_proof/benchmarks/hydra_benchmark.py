import statistics
import time

from ppci_sws_proof.hydra import simulate_hydra


def run_benchmark(iterations: int = 10_000) -> dict:
    latencies = []
    start = time.perf_counter()

    for index in range(iterations):
        capital = 50_000 + ((index % 25) * 20_000)
        risk_tolerance = (index % 10) / 10
        signal_intensity = ((index % 21) - 10) / 10

        iteration_start = time.perf_counter()
        simulate_hydra(capital, risk_tolerance, signal_intensity)
        latencies.append(time.perf_counter() - iteration_start)

    total_duration = time.perf_counter() - start
    throughput = iterations / total_duration if total_duration else 0.0

    return {
        "iterations": iterations,
        "total_duration_s": total_duration,
        "avg_latency_ms": statistics.mean(latencies) * 1000,
        "p95_latency_ms": statistics.quantiles(latencies, n=20)[18] * 1000,
        "throughput_per_s": throughput,
    }


if __name__ == "__main__":
    results = run_benchmark()
    print("Hydra benchmark results")
    print(f"Iterations      : {results['iterations']}")
    print(f"Total duration  : {results['total_duration_s']:.4f} s")
    print(f"Average latency : {results['avg_latency_ms']:.4f} ms")
    print(f"P95 latency     : {results['p95_latency_ms']:.4f} ms")
    print(f"Throughput      : {results['throughput_per_s']:.2f} simulations/s")

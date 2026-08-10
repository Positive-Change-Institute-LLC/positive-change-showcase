# core/routing_graph.py — Cross-Chain Routing Graph Analysis


def routing_graph(routes):
    route_count = len(routes)
    mev_exposure = "low" if route_count < 3 else "medium"

    return {
        "route_count": route_count,
        "mev_exposure": mev_exposure,
        "solver_network": "supported",
    }

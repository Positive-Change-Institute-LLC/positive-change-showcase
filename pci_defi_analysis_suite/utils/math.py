# utils/math.py — PCI DeFi Math Primitives


def invariant_xyk(x, y):
    return x * y


def price_impact(amount_in, reserve_in, reserve_out):
    return amount_in / (reserve_in + amount_in)

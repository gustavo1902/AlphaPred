from .base_model import base_probability
from .momentum import momentum_signal

def estimate_probability(event, history=None):
    base = base_probability(event)
    momentum = momentum_signal(event, history)

    return 0.8 * base + 0.2 * momentum
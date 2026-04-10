from src.alpha.engine import compute_alpha

def test_compute_alpha_positive():
    event = {"prob_market": 0.5}
    model_prob = 0.6
    assert compute_alpha(event, model_prob) == 0.1
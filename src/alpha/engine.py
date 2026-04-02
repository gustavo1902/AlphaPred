def compute_alpha(event, model_prob):
    return model_prob - event["prob_market"]

def generate_signal(alpha):
    if alpha > 0.1:
        return "STRONG_BUY"
    elif alpha > 0.03:
        return "BUY"
    elif alpha < -0.1:
        return "STRONG_SELL"
    elif alpha < -0.03:
        return "SELL"
    return "HOLD"
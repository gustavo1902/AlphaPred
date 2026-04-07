from src.ingestion.fetch_all import fetch_all_events
from src.normalization.normalize import normalize_events
from src.models.ensemble import estimate_probability
from src.alpha.engine import compute_alpha, generate_signal
from src.risk.filters import passes_filters

def run():
    events = fetch_all_events()
    events = normalize_events(events)

    results = []

    for event in events:
        if not passes_filters(event):
            continue

        prob_model = estimate_probability(event)
        alpha = compute_alpha(event, prob_model)
        signal = generate_signal(alpha)

        results.append({
            **event,
            "prob_model": prob_model,
            "alpha": alpha,
            "signal": signal
        })

    return results


if __name__ == "__main__":
    import json
    data = run()
    with open("data/signals.json", "w") as f:
        json.dump(data, f)
    print(json.dumps(data))
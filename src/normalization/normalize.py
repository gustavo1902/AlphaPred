def normalize_event(event):
    return {
        "id": event["id"],
        "question": event["question"],
        "prob_market": float(event["market_prob"]),
        "volume": float(event["volume"]),
        "source": event["source"]
    }

def normalize_events(events):
    return [normalize_event(e) for e in events]
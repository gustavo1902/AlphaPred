def base_probability(event):
    question = event["question"].lower()

    if "inflation" in question:
        return 0.7
    elif "rate" in question:
        return 0.6
    return 0.5
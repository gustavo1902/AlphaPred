def passes_filters(event):
    if event["volume"] < 1000:
        return False
    return True
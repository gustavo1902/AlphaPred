from .polymarket import fetch_polymarket_events
from .kalshi import fetch_kalshi_events

def fetch_all_events():
    events = []
    events.extend(fetch_polymarket_events())
    events.extend(fetch_kalshi_events())
    return events
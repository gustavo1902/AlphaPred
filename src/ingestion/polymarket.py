import requests

POLYMARKET_API = "https://api.polymarket.com/markets"

def fetch_polymarket_events():
    response = requests.get(POLYMARKET_API)
    data = response.json()

    events = []
    for market in data:
        events.append({
            "id": market["id"],
            "question": market["question"],
            "market_prob": float(market["outcomes"][0]["price"]),
            "volume": market.get("volume", 0),
            "source": "polymarket"
        })

    return events
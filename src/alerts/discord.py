import requests

def send_alert(webhook_url, event):
    message = f"""
🚨 Alpha Signal

Event: {event['question']}
Market: {event['prob_market']:.2f}
Model: {event['prob_model']:.2f}
Alpha: {event['alpha']:.2f}

Signal: {event['signal']}
"""

    requests.post(webhook_url, json={"content": message})
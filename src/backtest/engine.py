def run_backtest(events):
    pnl = 0
    trades = 0

    for e in events:
        if e["signal"] == "BUY":
            pnl += e["alpha"]  
            trades += 1

    return {
        "pnl": pnl,
        "trades": trades
    }
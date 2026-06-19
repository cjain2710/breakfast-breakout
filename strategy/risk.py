def risk_levels(signal, entry):
    if signal == "BUY":
        stop = entry * 0.98
        target = entry * 1.05

    elif signal == "SELL":
        stop = entry * 1.02
        target = entry * 0.95

    else:
        return None, None

    return round(stop, 2), round(target, 2)
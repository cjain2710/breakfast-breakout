def breakout_signal(df):

    if df is None or df.empty:
        return "WAIT", 0.0, None

    session = df.between_time("09:30", "10:30")

    if session.empty:
        return "WAIT", 0.0, None

    high = float(session["High"].max())
    low = float(session["Low"].min())

    price = float(df["Close"].iloc[-1])

    if price >= high:
        return "BUY", price, high

    if price <= low:
        return "SELL", price, low

    return "WAIT", price, None

def breakout_signal(df):

    if df is None or df.empty:
        return "WAIT", 0.0, None

    df = df.between_time("09:30", "10:15")

    if len(df) < 5:
        return "WAIT", 0.0, None

    # FIRST 5 CANDLES ONLY (important improvement)
    session = df.iloc[:5]

    high = float(session["High"].max())
    low = float(session["Low"].min())

    price = float(df["Close"].iloc[-1])

    # relaxed breakout logic
    if price > high * 1.001:
        return "BUY", price, high

    if price < low * 0.999:
        return "SELL", price, low

    return "WAIT", price, None

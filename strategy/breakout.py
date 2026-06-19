def breakfast_range(df):

    session = df.between_time("09:30", "10:30")

    high = float(session["High"].max())
    low = float(session["Low"].min())

    return high, low


def breakout_signal(df):

    high, low = breakfast_range(df)

    # IMPORTANT FIX: force scalar value
    price = float(df["Close"].iloc[-1])

    if price >= high:
        return "BUY", price, high

    if price <= low:
        return "SELL", price, low

    return "WAIT", price, None

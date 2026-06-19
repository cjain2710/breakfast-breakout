def breakfast_range(df):
    session = df.between_time("09:30", "10:30")

    high = session["High"].max()
    low = session["Low"].min()

    return high, low


def breakout_signal(df):
    high, low = breakfast_range(df)
    price = df["Close"].iloc[-1]

    if price > high:
        return "BUY", price, high

    if price < low:
        return "SELL", price, low

    return "WAIT", price, None
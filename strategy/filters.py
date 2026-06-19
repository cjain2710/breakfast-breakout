import pandas_ta as ta

def trend_filter(daily_df):
    if len(daily_df) < 200:
        return False

    daily_df["MA50"] = ta.sma(daily_df["Close"], length=50)
    daily_df["MA200"] = ta.sma(daily_df["Close"], length=200)

    latest = daily_df.iloc[-1]

    return latest["Close"] > latest["MA50"] > latest["MA200"]
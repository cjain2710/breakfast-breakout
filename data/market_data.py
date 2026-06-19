import yfinance as yf
import pandas as pd

def get_intraday(symbol):

    df = yf.download(
        symbol,
        period="5d",
        interval="15m",
        auto_adjust=True,
        progress=False
    )

    # 🔒 FIX 1: remove empty data
    if df is None or df.empty:
        return pd.DataFrame()

    # 🔒 FIX 2: flatten columns if needed
    df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]

    return df

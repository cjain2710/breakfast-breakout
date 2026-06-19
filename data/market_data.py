import yfinance as yf

def get_intraday(symbol):
    return yf.download(
        symbol,
        period="5d",
        interval="15m",
        auto_adjust=True
    )


def get_daily(symbol):
    return yf.download(
        symbol,
        period="1y",
        interval="1d",
        auto_adjust=True
    )
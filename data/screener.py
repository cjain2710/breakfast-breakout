from config.universe import UNIVERSE
from data.market_data import get_daily
from strategy.filters import trend_filter

def screen_stocks():
    selected = []

    for stock in UNIVERSE:
        try:
            df = get_daily(stock)

            if trend_filter(df):
                selected.append(stock)

        except:
            continue

    return selected
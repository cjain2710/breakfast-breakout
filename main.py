from dotenv import load_dotenv
load_dotenv()

from data.screener import screen_stocks
from data.market_data import get_intraday

from strategy.breakout import breakout_signal
from strategy.risk import risk_levels

from reports.generator import generate_report
from alerts.emailer import send_email


def run_engine():

    results = []

    # Step 1: Get filtered stock universe
    stocks = screen_stocks()

    print(f"Scanning {len(stocks)} stocks...")

    # Step 2: Process each stock
    for stock in stocks:

        try:
            df = get_intraday(stock)

            signal, price, level = breakout_signal(df)

            # Skip non-trading setups
            if signal == "WAIT":
                continue

            stop, target = risk_levels(signal, price)

            results.append({
                "Stock": stock,
                "Signal": signal,
                "Entry": round(price, 2),
                "Level": round(level, 2) if level else None,
                "Stop": round(stop, 2),
                "Target": round(target, 2)
            })

        except Exception as e:
            print(f"Error processing {stock}: {e}")

    # Step 3: Rank Top 10 signals (simple ranking by momentum proxy)
    results = sorted(results, key=lambda x: x["Entry"], reverse=True)[:10]

    # Step 4: Generate report
    file_path = generate_report(results)

    # Step 5: Email report only
    send_email(file_path)

    print("\n✅ Breakfast Breakout Engine Completed")
    print(f"Report saved at: {file_path}")


if __name__ == "__main__":
    run_engine()

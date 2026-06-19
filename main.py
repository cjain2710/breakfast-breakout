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

    stocks = screen_stocks()

    print(f"\n🚀 Starting Breakfast Breakout Engine")
    print(f"Scanning {len(stocks)} stocks...\n")

    if not stocks:
        print("❌ No stocks found in screener. Exiting safely.")
        return

    for stock in stocks:

        try:
            print(f"📊 Processing {stock}")

            df = get_intraday(stock)

            if df is None or df.empty:
                print(f"⚠️ No intraday data for {stock}")
                continue

            signal, price, level = breakout_signal(df)

            print(f"   Signal: {signal} | Price: {price}")

            if signal == "WAIT":
                continue

            stop, target = risk_levels(signal, price)

            results.append({
                "Stock": stock,
                "Signal": signal,
                "Entry": round(price, 2),
                "Level": round(level, 2) if level else None,
                "Stop": round(stop, 2) if stop else None,
                "Target": round(target, 2) if target else None
            })

        except Exception as e:
            print(f"❌ Error processing {stock}: {str(e)}")

    # Ensure stable output even if no trades
    if not results:
        print("\n⚠️ No breakout signals generated today.")

        results.append({
            "Stock": "NO TRADE",
            "Signal": "WAIT",
            "Entry": 0,
            "Level": 0,
            "Stop": 0,
            "Target": 0
        })

    # Sort (optional: strongest first)
    results = sorted(results, key=lambda x: x["Entry"], reverse=True)[:10]

    print("\n📄 Generating report...")

    file_path = generate_report(results)

    print(f"📧 Sending email: {file_path}")

    try:
        send_email(file_path)
        print("✅ Email sent successfully")
    except Exception as e:
        print(f"❌ Email failed: {str(e)}")

    print("\n🏁 Breakfast Breakout Engine Completed")


if __name__ == "__main__":
    run_engine()

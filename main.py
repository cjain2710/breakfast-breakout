from dotenv import load_dotenv
load_dotenv()

from data.screener import screen_stocks
from data.market_data import get_intraday

from strategy.breakout import breakout_signal
from strategy.risk import risk_levels

from reports.generator import generate_report
from alerts.emailer import send_email
from alerts.whatsapp import send_whatsapp

results = []

stocks = screen_stocks()

for stock in stocks:

    try:
        df = get_intraday(stock)

        signal, price, level = breakout_signal(df)

        if signal == "WAIT":
            continue

        stop, target = risk_levels(signal, price)

        results.append({
            "Stock": stock,
            "Signal": signal,
            "Entry": price,
            "Level": level,
            "Stop": stop,
            "Target": target
        })

    except:
        continue

results = results[:10]

file_path = generate_report(results)

send_email(file_path)

msg = "\n".join([
    f"{r['Stock']} {r['Signal']} @ {r['Entry']}"
    for r in results
])

send_whatsapp(msg)

print("Done")


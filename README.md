\# Breakfast Breakout Engine



Daily US stock breakout scanner that:

\- Finds top 10 breakout setups

\- Uses trend + volume filters

\- Sends email + WhatsApp alerts at 9:45 AM



\## Setup



\### Install

pip install -r requirements.txt



\### Environment

cp .env.example .env

Fill credentials



\### Run manually

python main.py



\## Automate (Linux / Oracle Cloud)

crontab -e



45 0 \* \* 2-6 python3 /home/ubuntu/breakfast-breakout/main.py


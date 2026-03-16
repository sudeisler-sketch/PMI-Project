

import yfinance as yf

pm_data = yf.download("PM", start="2008-03-17", end="2026-03-16", interval="1mo")

print(pm_data.head())

print(pm_data.tail())

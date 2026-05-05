import yfinance as yf
import pandas as pd


START_DATE = "2008-03-17"
END_DATE = "2026-03-16"


pm_data = yf.download("PM", start=START_DATE, end=END_DATE, interval="1wk")
sp500_data = yf.download("^GSPC", start=START_DATE, end=END_DATE, interval="1wk")
treasury_data = yf.download("^TNX", start=START_DATE, end=END_DATE, interval="1wk")
oil_data = yf.download("CL=F", start=START_DATE, end=END_DATE, interval="1wk")
treasury_data = yf.download("^TNX", start=START_DATE, end=END_DATE, interval="1wk")


print("PM columns:", pm_data.columns)
print("SP500 columns:", sp500_data.columns)

pm_price_col = "Adj Close" if "Adj Close" in pm_data.columns else "Close"
sp500_price_col = "Adj Close" if "Adj Close" in sp500_data.columns else "Close"
treasury_price_col = "Adj Close" if "Adj Close" in treasury_data.columns else "Close"

pm_data = pm_data[[pm_price_col, "Volume"]].copy()
sp500_data = sp500_data[[sp500_price_col]].copy()
treasury_data = treasury_data[[treasury_price_col]].copy()

pm_data.columns = ["PM_adj_close", "PM_volume"]
sp500_data.columns = ["SP500_adj_close"]
treasury_data.columns = ["Treasury_10Y_yield"]

pm_data.reset_index(inplace=True)
sp500_data.reset_index(inplace=True)
treasury_data.reset_index(inplace=True)

merged_data = pd.merge(pm_data, sp500_data, on="Date", how="inner")
merged_data = pd.merge(merged_data, treasury_data, on="Date", how="inner")


merged_data["PM_return"] = merged_data["PM_adj_close"].pct_change()
merged_data["SP500_return"] = merged_data["SP500_adj_close"].pct_change()
merged_data["Treasury_10Y_change"] = merged_data["Treasury_10Y_yield"].diff()


merged_data.dropna(inplace=True)

merged_data.to_csv("pmi_project_data.csv", index=False)

print(merged_data.head())
print(merged_data.tail())
print("Shape of dataset:", merged_data.shape)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pmi_weekly_project_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

print("First 5 rows:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())

print("\nCorrelation matrix:")
print(df[["PM_adj_close", "SP500_adj_close", "PM_return", "SP500_return"]].corr())

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["PM_adj_close"])
plt.title("PMI Weekly Adjusted Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("PMI Adjusted Close")
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["SP500_adj_close"])
plt.title("S&P 500 Weekly Adjusted Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("S&P 500 Adjusted Close")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["PM_return"], bins=30)
plt.title("Distribution of PMI Weekly Returns")
plt.xlabel("PMI Weekly Return")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["PM_return"], label="PMI Weekly Return")
plt.plot(df["Date"], df["SP500_return"], label="S&P 500 Weekly Return")
plt.title("PMI vs S&P 500 Weekly Returns")
plt.xlabel("Date")
plt.ylabel("Return")
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load sentiment results
sentiment_df = pd.read_csv("data/sentiment_results.csv")

# Load stock prices and get latest close price
stocks = ["TSLA", "NVDA", "AAPL", "AMZN", "MSFT"]
price_data = []

for ticker in stocks:
    df = pd.read_csv(f"data/{ticker}_price.csv")
    latest_price = df["Close"].iloc[-1]
    avg_price = df["Close"].mean()
    price_change = ((df["Close"].iloc[-1] - df["Close"].iloc[0]) / df["Close"].iloc[0]) * 100
    price_data.append({
        "ticker": ticker,
        "latest_price": round(latest_price, 2),
        "avg_price": round(avg_price, 2),
        "price_change_percent": round(price_change, 2)
    })

price_df = pd.DataFrame(price_data)

# Calculate average sentiment score per stock
sentiment_avg = sentiment_df.groupby("ticker")["score"].mean().reset_index()
sentiment_avg.columns = ["ticker", "avg_sentiment"]

# Merge both dataframes
merged = pd.merge(price_df, sentiment_avg, on="ticker")
print("=== Correlation Table ===")
print(merged)

# Save merged data
merged.to_csv("data/correlation_results.csv", index=False)

# Plot chart
fig, ax1 = plt.subplots(figsize=(10, 6))

x = range(len(merged))
ax1.bar(x, merged["price_change_percent"], color="skyblue", label="Price Change %")
ax1.set_xlabel("Stock")
ax1.set_ylabel("Price Change %", color="blue")
ax1.set_xticks(x)
ax1.set_xticklabels(merged["ticker"])

ax2 = ax1.twinx()
ax2.plot(x, merged["avg_sentiment"], color="red", marker="o", linewidth=2, label="Avg Sentiment")
ax2.set_ylabel("Avg Sentiment Score", color="red")

plt.title("Stock Price Change vs Sentiment Score")
fig.legend(loc="upper left")
plt.tight_layout()
plt.savefig("data/correlation_chart.png")
plt.show()
print("Chart saved!")

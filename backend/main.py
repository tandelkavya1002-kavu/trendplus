from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route 1 - Home
@app.get("/")
def home():
    return {"message": "TrendPulse API is running!"}

# Route 2 - Get all stocks
@app.get("/stocks")
def get_stocks():
    stocks = ["TSLA", "NVDA", "AAPL", "AMZN", "MSFT"]
    data = []
    for ticker in stocks:
        df = pd.read_csv(f"data/{ticker}_price.csv")
        data.append({
            "ticker": ticker,
            "latest_price": round(df["Close"].iloc[-1], 2),
            "price_change": round(((df["Close"].iloc[-1] - df["Close"].iloc[0]) / df["Close"].iloc[0]) * 100, 2)
        })
    return {"stocks": data}

# Route 3 - Get sentiment
@app.get("/sentiment/{ticker}")
def get_sentiment(ticker: str):
    df = pd.read_csv("data/sentiment_results.csv")
    filtered = df[df["ticker"] == ticker.upper()]
    return {"ticker": ticker, "sentiment": filtered.to_dict(orient="records")}

# Route 4 - Get correlation
@app.get("/correlation")
def get_correlation():
    df = pd.read_csv("data/correlation_results.csv")
    return {"correlation": df.to_dict(orient="records")}

# Route 5 - Trending stocks
@app.get("/trending")
def get_trending():
    df = pd.read_csv("data/correlation_results.csv")
    df = df.sort_values("price_change_percent", ascending=False)
    top = df.head(3)
    return {"trending": top.to_dict(orient="records")}

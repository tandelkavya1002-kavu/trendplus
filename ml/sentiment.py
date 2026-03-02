from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Create analyzer
analyzer = SentimentIntensityAnalyzer()

# Sample stock related news/posts
news = [
    {"ticker": "TSLA", "text": "Tesla hits record sales this quarter! Amazing growth!"},
    {"ticker": "TSLA", "text": "Tesla stock crashes after CEO controversy"},
    {"ticker": "NVDA", "text": "Nvidia GPU demand explodes due to AI boom"},
    {"ticker": "AAPL", "text": "Apple faces lawsuit over patent issues"},
    {"ticker": "MSFT", "text": "Microsoft Azure cloud revenue up 30 percent"},
    {"ticker": "AMZN", "text": "Amazon lays off thousands of employees"},
    {"ticker": "NVDA", "text": "Nvidia beats earnings expectations massively"},
    {"ticker": "TSLA", "text": "Tesla new model receives terrible reviews"},
]

# Analyze each news item
results = []
for item in news:
    score = analyzer.polarity_scores(item["text"])
    
    # Label sentiment
    if score["compound"] >= 0.05:
        label = "Positive"
    elif score["compound"] <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"
    
    results.append({
        "ticker": item["ticker"],
        "text": item["text"],
        "score": round(score["compound"], 3),
        "sentiment": label
    })
    
    print(f"{item['ticker']} → {label} ({score['compound']})")
    print(f"  {item['text']}")
    print()

# Save results
df = pd.DataFrame(results)
df.to_csv("data/sentiment_results.csv", index=False)
print("Sentiment results saved!")


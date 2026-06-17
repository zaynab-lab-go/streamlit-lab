import pandas as pd
import requests
from textblob import TextBlob

# =========================
# GitHub data
# =========================
def fetch_github(search_term):
    url = f"https://api.github.com/search/repositories?q={search_term}"
    r = requests.get(url)

    if r.status_code != 200:
        return pd.DataFrame()

    data = r.json()
    results = []

    for item in data.get("items", []):
        results.append({
            "source": "GitHub",
            "name": item.get("name"),
            "stars": item.get("stargazers_count", 0),
            "language": item.get("language") or "Unknown",
            "score": item.get("score", 0)
        })

    return pd.DataFrame(results)


# =========================
# ProductHunt mock
# =========================
def fetch_producthunt(search_term):
    data = [
        {"source": "ProductHunt", "name": "AI Tool X", "stars": 1200, "language": "AI", "score": 4.8},
        {"source": "ProductHunt", "name": "Dev Tool Y", "stars": 980, "language": "Dev", "score": 4.5},
        {"source": "ProductHunt", "name": "Startup Z", "stars": 1500, "language": "Startup", "score": 4.9},
    ]
    return pd.DataFrame(data)


# =========================
# Merge dataset
# =========================
def fetch_all_data(search_term):
    df = pd.concat([
        fetch_github(search_term),
        fetch_producthunt(search_term)
    ], ignore_index=True)

    if df.empty:
        return df

    df.columns = [c.lower() for c in df.columns]

    for col in ["source", "name", "stars", "language", "score"]:
        if col not in df.columns:
            df[col] = 0 if col in ["stars", "score"] else "unknown"

    return df


# =========================
# Sentiment
# =========================
def fetch_reviews(app_name):
    return [
        f"{app_name} is great",
        f"I like {app_name}",
        f"{app_name} is bad sometimes",
        f"Amazing experience with {app_name}"
    ]


def analyze_sentiment(text):
    score = TextBlob(text).sentiment.polarity

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    return "neutral"

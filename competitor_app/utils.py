import pandas as pd
import requests

# =========================================================
# 1. GITHUB API (DATA SOURCE)
# =========================================================
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


# =========================================================
# 2. PRODUCTHUNT MOCK DATA
# =========================================================
def fetch_producthunt(search_term):
    data = [
        {"source": "ProductHunt", "name": "AI Tool X", "stars": 1200, "language": "AI", "score": 4.8},
        {"source": "ProductHunt", "name": "Dev Tool Y", "stars": 980, "language": "Dev", "score": 4.5},
        {"source": "ProductHunt", "name": "Startup Z", "stars": 1500, "language": "Startup", "score": 4.9},
    ]
    return pd.DataFrame(data)


# =========================================================
# 3. MERGED DATASET (SAFE STRUCTURE)
# =========================================================
def fetch_all_data(search_term):
    df = pd.concat([
        fetch_github(search_term),
        fetch_producthunt(search_term)
    ], ignore_index=True)

    if df.empty:
        return df

    # standardize columns
    df.columns = [c.lower() for c in df.columns]

    required = ["source", "name", "stars", "language", "score"]

    for col in required:
        if col not in df.columns:
            df[col] = 0 if col in ["stars", "score"] else "unknown"

    return df


# =========================================================
# 4. SENTIMENT (NO TORCH / NO TORCHVISION VERSION)
# =========================================================

# IMPORTANT: use lightweight pipeline only
from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"   # keeps it stable
)


# =========================================================
# 5. FAKE REVIEWS (SAFE FOR LAB)
# =========================================================
def fetch_reviews(app_name):
    return [
        f"{app_name} is amazing and very useful",
        f"I hate using {app_name}, it's too slow",
        f"{app_name} works perfectly fine",
        f"Very bad experience with {app_name}",
        f"I really love this app"
    ]


# =========================================================
# 6. SENTIMENT ANALYSIS PER REVIEW
# =========================================================
def analyze_reviews(reviews):
    results = []

    for r in reviews:
        pred = sentiment_model(r)[0]

        results.append({
            "review": r,
            "label": pred["label"],
            "score": float(pred["score"])
        })

    return pd.DataFrame(results)


# =========================================================
# 7. GLOBAL SENTIMENT SCORE
# =========================================================
def compute_app_sentiment(df_reviews):
    if df_reviews.empty:
        return 0

    positive = df_reviews[df_reviews["label"] == "POSITIVE"].shape[0]
    return positive / len(df_reviews)
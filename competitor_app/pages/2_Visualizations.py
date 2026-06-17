import streamlit as st
import pandas as pd
import plotly.express as px
from utils import fetch_all_data, fetch_reviews, analyze_sentiment

st.set_page_config(page_title="Visualizations", layout="wide")

st.title("📊 Competitor Analysis Dashboard")

# =========================
# LOAD DATA
# =========================
query = st.text_input("Enter a keyword to analyze", "ai")

if query:
    df = fetch_all_data(query)

    if df.empty:
        st.warning("No data found.")
        st.stop()

    st.success(f"{len(df)} competitors loaded")

    # =========================
    # PREPROCESS
    # =========================
    df["stars"] = pd.to_numeric(df["stars"], errors="coerce")
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    # =========================
    # SENTIMENT DATA (mock reviews)
    # =========================
    all_reviews = []
    for name in df["name"].unique():
        reviews = fetch_reviews(name)
        for r in reviews:
            all_reviews.append({
                "app": name,
                "review": r,
                "sentiment": analyze_sentiment(r)
            })

    df_reviews = pd.DataFrame(all_reviews)

    # =========================
    # 1. BAR CHART - STARS BY APP
    # =========================
    st.subheader("⭐ 1. Popularity (Stars by App)")
    fig1 = px.bar(df, x="name", y="stars", color="source", title="Stars Comparison")
    st.plotly_chart(fig1, use_container_width=True)

    # =========================
    # 2. PIE CHART - SOURCES DISTRIBUTION
    # =========================
    st.subheader("📦 2. Data Sources Distribution")
    fig2 = px.pie(df, names="source", title="GitHub vs ProductHunt")
    st.plotly_chart(fig2, use_container_width=True)

    # =========================
    # 3. TOP LANGUAGES / CATEGORIES
    # =========================
    st.subheader("🧠 3. Technologies / Categories Used")
    lang_count = df["language"].value_counts().reset_index()
    lang_count.columns = ["language", "count"]

    fig3 = px.bar(lang_count, x="language", y="count", color="language")
    st.plotly_chart(fig3, use_container_width=True)

    # =========================
    # 4. SCATTER - SCORE VS STARS
    # =========================
    st.subheader("📈 4. Quality vs Popularity")
    fig4 = px.scatter(
        df,
        x="stars",
        y="score",
        color="source",
        size="stars",
        hover_name="name",
        title="Stars vs Score"
    )
    st.plotly_chart(fig4, use_container_width=True)

    # =========================
    # 5. HEATMAP STYLE (Correlation)
    # =========================
    st.subheader("🔥 5. Correlation Heatmap")
    corr = df[["stars", "score"]].corr()
    fig5 = px.imshow(corr, text_auto=True, title="Correlation Matrix")
    st.plotly_chart(fig5, use_container_width=True)

    # =========================
    # 6. SENTIMENT DISTRIBUTION
    # =========================
    st.subheader("💬 6. User Sentiment Analysis")
    sentiment_count = df_reviews["sentiment"].value_counts().reset_index()
    sentiment_count.columns = ["sentiment", "count"]

    fig6 = px.bar(
        sentiment_count,
        x="sentiment",
        y="count",
        color="sentiment",
        title="Overall Sentiment"
    )
    st.plotly_chart(fig6, use_container_width=True)

    # =========================
    # 7. SENTIMENT BY APP
    # =========================
    st.subheader("🧩 7. Sentiment per App")

    sentiment_app = df_reviews.groupby(["app", "sentiment"]).size().reset_index(name="count")

    fig7 = px.bar(
        sentiment_app,
        x="app",
        y="count",
        color="sentiment",
        barmode="group",
        title="Sentiment Comparison per App"
    )
    st.plotly_chart(fig7, use_container_width=True)

    # =========================
    # RAW DATA EXPANDER
    # =========================
    with st.expander("📄 View Raw Data"):
        st.dataframe(df, use_container_width=True)

    with st.expander("💬 View Reviews Data"):
        st.dataframe(df_reviews, use_container_width=True)

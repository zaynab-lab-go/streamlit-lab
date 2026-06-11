import streamlit as st
import plotly.express as px
from utils import fetch_reviews, analyze_reviews, compute_app_sentiment

st.title("🧠 Sentiment Analysis")

# ---------------- CHECK ----------------
if "data" not in st.session_state:
    st.warning("Run SEARCH page first")
    st.stop()

df = st.session_state["data"]

st.success("Data loaded successfully")

# ---------------- SELECT APP ----------------
app_names = df["name"].dropna().unique()

if len(app_names) == 0:
    st.error("No apps available")
    st.stop()

selected_app = st.selectbox("Select app", app_names)

# ---------------- PROCESS ----------------
reviews = fetch_reviews(selected_app)
df_reviews = analyze_reviews(reviews)

score = compute_app_sentiment(df_reviews)

st.metric("Positive Score", f"{score:.2f}")

# ---------------- CHARTS ----------------
fig = px.pie(df_reviews, names="label", title="Sentiment Distribution")
st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(df_reviews, x="review", y="score", color="label")
st.plotly_chart(fig2, use_container_width=True)

st.dataframe(df_reviews)
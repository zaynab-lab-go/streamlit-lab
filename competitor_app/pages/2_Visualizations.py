import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Visualizations", layout="wide")

st.title("📊 Analytics Dashboard")

# ==========================================
# CHECK DATA
# ==========================================
if "data" not in st.session_state:
    st.warning("⚠️ Please search first in Search page")
    st.stop()

df = st.session_state["data"]

if df.empty:
    st.warning("No data available")
    st.stop()

# ==========================================
# SIDEBAR FILTERS
# ==========================================
st.sidebar.header("🎛️ Filters")

# Filter source
selected_sources = st.sidebar.multiselect(
    "Source",
    df["source"].unique()
)

if selected_sources:
    df = df[df["source"].isin(selected_sources)]

# Filter language
selected_languages = st.sidebar.multiselect(
    "Language",
    df["language"].dropna().unique()
)

if selected_languages:
    df = df[df["language"].isin(selected_languages)]

# ==========================================
# KPIs
# ==========================================
col1, col2, col3 = st.columns(3)

col1.metric("📦 Total Results", len(df))
col2.metric("⭐ Max Stars", int(df["stars"].max()))
col3.metric("🌍 Languages", df["language"].nunique())

st.divider()

# ==========================================
# TOP APPS / REPOS
# ==========================================
st.subheader("🏆 Top Results by Stars")

top = df.sort_values("stars", ascending=False).head(10)

fig = px.bar(
    top,
    x="stars",
    y="name",
    color="source",
    orientation="h"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# PIE CHART
# ==========================================
st.subheader("📊 Source Distribution")

fig2 = px.pie(
    df,
    names="source"
)

st.plotly_chart(fig2, use_container_width=True)

# ==========================================
# LANGUAGE DISTRIBUTION
# ==========================================
st.subheader("💻 Programming Languages")

lang_counts = df["language"].value_counts().reset_index()
lang_counts.columns = ["language", "count"]

fig3 = px.bar(
    lang_counts,
    x="language",
    y="count"
)

st.plotly_chart(fig3, use_container_width=True)

# ==========================================
# BOXPLOT
# ==========================================
st.subheader("📦 Stars Distribution")

fig4 = px.box(
    df,
    x="source",
    y="stars",
    color="source"
)

st.plotly_chart(fig4, use_container_width=True)

# ==========================================
# HEATMAP
# ==========================================
st.subheader("🔥 Correlation Heatmap")

corr = df[["stars", "score"]].corr()

fig5 = px.imshow(
    corr,
    text_auto=True
)

st.plotly_chart(fig5, use_container_width=True)

# ==========================================
# DOWNLOAD BUTTON
# ==========================================
st.download_button(
    "📥 Download CSV",
    df.to_csv(index=False),
    file_name="results.csv"
)
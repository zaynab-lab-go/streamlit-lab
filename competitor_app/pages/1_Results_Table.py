import streamlit as st
from utils import fetch_all_data

st.set_page_config(page_title="Search", layout="wide")

st.title("🔎 Smart App Search Engine")

st.markdown("### 💡 Example Searches")

examples = {
    "🤖 AI": "ai",
    "🐍 Python": "python",
    "🧠 Machine Learning": "machine learning",
    "🚀 Startup": "startup",
    "🎮 Games": "games",
    "📱 Mobile Apps": "mobile"
}

cols = st.columns(3)

for i, (label, value) in enumerate(examples.items()):
    if cols[i % 3].button(label):
        st.session_state["query"] = value


query = st.text_input(
    "Search",
    value=st.session_state.get("query", ""),
    placeholder="Ex: ai, python..."
)

if query:

    with st.spinner("Loading data..."):
        df = fetch_all_data(query)

    if not df.empty:

        st.session_state["data"] = df

        st.success(f"✅ {len(df)} results found")

        st.dataframe(df, use_container_width=True)

    else:
        st.error("No results found")
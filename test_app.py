import streamlit as st
import pandas as pd
from datetime import date, time

st.set_page_config(page_title="Streamlit Widgets Tour", layout="wide")

# ─────────────────────────────────────────
# 1. DISPLAY WIDGETS
# ─────────────────────────────────────────
st.title("🧩 Streamlit Widgets Tour")
st.header("1. Display Widgets")
st.code("print('Hello, Streamlit!')", language="python")

st.divider()

# ─────────────────────────────────────────
# 2. INPUT WIDGETS
# ─────────────────────────────────────────
st.header("2. Input Widgets")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Your name", placeholder="e.g. Zaynab")
    bio  = st.text_area("Short bio", placeholder="Tell us about yourself...")
    age  = st.number_input("Your age", min_value=0, max_value=100, value=20)

with col2:
    birthday  = st.date_input("Birthday", value=date(2005, 7, 5))

if name:
    st.success(f"Hello, **{name}**! You are {age} years old.")

st.divider()

# ─────────────────────────────────────────
# 3. FILE WIDGET
# ─────────────────────────────────────────
st.header("3. File Upload")

uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.write(f"✅ File loaded — {df.shape[0]} rows × {df.shape[1]} columns")
    st.dataframe(df.head())

st.divider()

# ─────────────────────────────────────────
# 4. FILTER WIDGETS
# ─────────────────────────────────────────
st.header("4. Filter Widgets")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Single choice")
    agree    = st.checkbox("I agree to the terms")
    toggle   = st.toggle("Dark mode")
    gender   = st.radio("Gender", ["Male", "Female"])
    country  = st.selectbox("Country", ["Morocco", "France", "USA", "Spain"])
    score    = st.slider("Satisfaction score", 0, 10, 7)

with col4:
    st.subheader("Multiple choice")
    langs    = st.multiselect("Languages you know",
                              ["Python", "R", "SQL", "JavaScript", "Java"],
                              default=["Python"])
    priority = st.select_slider("Priority level",
                                options=["Low", "Medium", "High", "Critical"],
                                value="Medium")

st.write({
    "Agreed": agree, "Dark mode": toggle, "Gender": gender,
    "Country": country, "Score": score, "Languages": langs, "Priority": priority
})

st.divider()

# ─────────────────────────────────────────
# 5. BUTTON WIDGETS
# ─────────────────────────────────────────
st.header("5. Button Widgets")

col5, col6, col7 = st.columns(3)

with col5:
    if st.button("Click me!"):
        st.balloons()

with col6:
    sample_csv = "name,score\nAlice,95\nBob,87\nCarol,92"
    st.download_button("⬇️ Download sample CSV",
                       data=sample_csv,
                       file_name="sample.csv",
                       mime="text/csv")

with col7:
    st.link_button("📚 Streamlit Docs", "https://docs.streamlit.io")

st.divider()

# ─────────────────────────────────────────
# 6. DATA WIDGETS
# ─────────────────────────────────────────
st.header("6. Data Widgets")

sample_df = pd.DataFrame({
    "Company":  ["Apple", "Google", "Microsoft", "Amazon"],
    "Revenue":  [394, 283, 211, 514],
    "Growth %": [8.1, 6.4, 10.2, 9.3],
    "Website":  [
        "https://apple.com",
        "https://google.com",
        "https://microsoft.com",
        "https://amazon.com"
    ]
})

st.subheader("st.dataframe — with column config")
st.dataframe(
    sample_df,
    column_config={
        "Revenue":  st.column_config.NumberColumn("Revenue ($B)", format="$%d B"),
        "Growth %": st.column_config.ProgressColumn("Growth %", min_value=0, max_value=20),
        "Website":  st.column_config.LinkColumn("Website"),
    },
    use_container_width=True
)

st.subheader("st.data_editor — editable table")
edited = st.data_editor(sample_df, use_container_width=True, num_rows="dynamic")
st.write("Edited data:", edited)

st.divider()

# ─────────────────────────────────────────
# 7. OTHER WIDGETS
# ─────────────────────────────────────────
st.header("7. Other Widgets")

fav_color = st.color_picker("Pick your favorite color", "#00B4D8")
st.markdown(f"Your color: <span style='color:{fav_color}; font-size:24px'>■</span> `{fav_color}`",
            unsafe_allow_html=True)

st.divider()


import pandas as pd

# ─────────────────────────────────────────
# STREAMLIT MAGIC
# ─────────────────────────────────────────

"## ✨ Streamlit Magic"

df = pd.DataFrame({
    "Company":  ["Apple", "Google", "Microsoft", "Amazon"],
    "Revenue":  [394, 283, 211, 514],
    "Growth %": [8.1, 6.4, 10.2, 9.3]
})
df


# ─────────────────────────────────────────
# UX DESIGN — LAYOUTS & CONTAINERS
# ─────────────────────────────────────────
st.title("🎨 UX Design — Layouts & Containers")

# ── 1. SIDEBAR ──────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")
    theme     = st.selectbox("Theme", ["Light", "Dark", "Custom"])
    show_data = st.checkbox("Show raw data", value=True)
    st.markdown("---")
    st.caption("Streamlit Layout Demo")

# ── 2. COLUMNS ──────────────────────────
st.header("📐 Columns")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Revenue", value="$394B", delta="+8.1%")

with col2:
    st.metric(label="Users", value="2.1B", delta="+5.3%")

with col3:
    st.metric(label="Market Share", value="27%", delta="-1.2%")

# ── 3. TABS ─────────────────────────────
st.header("📑 Tabs")
tab1, tab2, tab3 = st.tabs(["📊 Data", "📈 Charts", "ℹ️ Info"])

with tab1:
    st.write("Data content here")
    if show_data:
        st.dataframe(df)

with tab2:
    st.write("Charts content here")
    st.line_chart(df.set_index("Company")["Revenue"])

with tab3:
    st.write("Info content here")
    st.info("This app demonstrates Streamlit layouts.")

# ── 4. EXPANDER ─────────────────────────
st.header("🔽 Expander")
with st.expander("Click to expand — see raw data"):
    st.json({
        "companies": ["Apple", "Google", "Microsoft"],
        "revenues":  [394, 283, 211]
    })

# ── 5. CONTAINER ────────────────────────
st.header("📦 Container")
with st.container(border=True):
    st.subheader("Grouped content")
    c1, c2 = st.columns(2)
    with c1:
        st.write("Left side content")
        st.success("✅ Status: Active")
    with c2:
        st.write("Right side content")
        st.warning("⚠️ Warning: Check data")

# ── 6. EMPTY PLACEHOLDER ────────────────
st.header("⏳ Empty Placeholder")
placeholder = st.empty()
if st.button("Fill the placeholder"):
    placeholder.success("🎉 Placeholder is now filled!")
else:
    placeholder.info("Click the button above to fill me!")
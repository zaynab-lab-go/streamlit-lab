import streamlit as st

st.set_page_config(
    page_title='Competitor Analysis App',
    page_icon='🔍',
    layout='wide'
)

st.markdown('''
<div style='text-align: center; padding: 20px 0;'>
    <h1 style='font-size: 48px;'>🔍 Competitor Analysis Dashboard</h1>
    <p style='font-size: 20px; color: #888;'>Know your market. Outsmart your competitors. Make data-driven decisions.</p>
</div>
''', unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('''
    ### 🧩 The Challenge
    Imagine you're launching a new app. You know your idea is great...
    but so do **dozens of competitors** already on the market.

    - Which apps are leading the race? 🏆
    - What do users actually think of them? 💬
    - Where are the gaps you could fill? 🕳️
    ''')

with col2:
    st.markdown('''
    ### 💡 The Solution
    This app turns guesswork into **insight**. In just 2 clicks, you get:

    - 📊 A full competitor breakdown
    - 📈 Visual comparisons of ratings, reviews & pricing
    - 🧠 AI-powered sentiment analysis of real user reviews
    ''')

st.divider()

st.markdown('### 🚀 How it works')

step1, step2, step3 = st.columns(3)

card_style = 'background-color:#D6E4FF; color:#111111; padding:20px; border-radius:12px; text-align:center; min-height:200px;'

with step1:
    st.markdown(f'''
    <div style='{card_style}'>
    <h2 style='color:#111111;'>1️⃣</h2>
    <h4 style='color:#111111;'>Search</h4>
    <p style='color:#222222; font-size:14px;'>Pick a category or type your own query (e.g. <i>fitness tracking apps</i>)</p>
    </div>
    ''', unsafe_allow_html=True)

with step2:
    st.markdown(f'''
    <div style='{card_style}'>
    <h2 style='color:#111111;'>2️⃣</h2>
    <h4 style='color:#111111;'>Explore</h4>
    <p style='color:#222222; font-size:14px;'>Dive into ratings, prices and reviews in interactive charts</p>
    </div>
    ''', unsafe_allow_html=True)

with step3:
    st.markdown(f'''
    <div style='{card_style}'>
    <h2 style='color:#111111;'>3️⃣</h2>
    <h4 style='color:#111111;'>Understand</h4>
    <p style='color:#222222; font-size:14px;'>Let AI read the reviews and reveal what users <i>really</i> feel</p>
    </div>
    ''', unsafe_allow_html=True)

st.divider()

st.markdown('''
<div style='text-align:center; padding: 20px;'>
    <h3>👈 Ready? Head to <b>Search</b> in the sidebar to begin!</h3>
</div>
''', unsafe_allow_html=True)

st.info('💡 Tip: Try the quick-pick buttons on the Search page for instant demos.')

import streamlit as st
import joblib

st.set_page_config(
    page_title="Fake News Detection",
    layout="centered"
)

st.title("📰 Fake News Detection System")
st.markdown(
    "Enter a news article below to check whether it is **Real** or **Fake**."
)

# Load model
model = joblib.load("fake_news_pipeline.pkl")

user_input = st.text_area(
    "📝 News Article Text",
    height=250,
    placeholder="Paste the full news article here..."
)

if st.button("🔍 Analyze News"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        prediction = model.predict([user_input])[0]
        confidence = model.predict_proba([user_input]).max()

        st.markdown("---")
        if prediction == 1:
            st.success(f"✅ **Real News**\n\nConfidence: **{confidence:.2%}**")
        else:
            st.error(f"❌ **Fake News**\n\nConfidence: **{confidence:.2%}**")


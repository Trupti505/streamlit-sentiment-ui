import streamlit as st
import requests

st.set_page_config(page_title="Sentiment Predictor", layout="centered")
st.title("🎬 Movie Review Sentiment Analyzer")

st.markdown("Enter a movie review below to see if it's **positive** or **negative**.")

# Text input
user_input = st.text_area("📝 Your Review", height=200)

if st.button("Predict Sentiment"):
    if not user_input.strip():
        st.warning("Please enter a review before submitting.")
    else:
        with st.spinner("Analyzing..."):
            response = requests.post(
                "https://sentiment-api-owpg.onrender.com/predict",
                json={"review": user_input}
            )

            if response.status_code == 200:
                sentiment = response.json()["sentiment"]
                emoji = "👍" if sentiment == "positive" else "👎"
                st.success(f"**Sentiment:** {sentiment.capitalize()} {emoji}")
            else:
                st.error("Something went wrong with the API call.")

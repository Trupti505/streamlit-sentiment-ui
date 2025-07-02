# Sentiment Analyzer App

A full-stack NLP web app that predicts the **sentiment** (positive/negative) of a movie review using a trained logistic regression model and TF-IDF features.

---

## Live Demo

🌐 Frontend (Streamlit): [Try the App](https://app-sentiment-ui-cb44uarrt6astapped3pgkv.streamlit.app/)  
🔗 Backend (FastAPI): [API Docs](https://sentiment-api-owpg.onrender.com/docs)

---

## How It Works

1. **User** types a movie review into the frontend
2. Streamlit sends it to a **FastAPI** endpoint hosted on Render
3. The API:
   - Uses a saved **TF-IDF vectorizer**
   - Loads a trained **Logistic Regression model**
   - Returns `"positive"` or `"negative"` sentiment
4. The prediction is shown with an emoji on the UI

---

##  Tech Stack

- **Python**
- **Scikit-learn** (for training)
- **FastAPI** (API backend)
- **Streamlit** (UI frontend)
- **Render** (for API deployment)
- **Streamlit Cloud** (for UI deployment)

---

## 📁 Project Structure

```text
.
├── app.py                 # FastAPI backend
├── sentiment_model.pkl    # Trained logistic regression model
├── tfidf_vectorizer.pkl   # Saved TF-IDF vectorizer
├── streamlit_app.py       # Streamlit UI
├── requirements.txt       # All dependencies
└── README.md              # Project overview






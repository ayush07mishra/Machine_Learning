import re
import pandas as pd
from textblob import TextBlob
import streamlit as st
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www.\S+', '', text)
    text = re.sub(r'@\w+|#\w+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    tokens = text.split()
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'Positive 😊'
    elif polarity < 0:
        return 'Negative 😠'
    else:
        return 'Neutral 😐'

st.title("Twitter Sentiment Analyzer")
user_input = st.text_area("Enter a tweet:")

if st.button("Analyze Sentiment"):
    cleaned_text = preprocess_text(user_input)
    result = get_sentiment(cleaned_text)
    st.write(f"**Sentiment:** {result}")

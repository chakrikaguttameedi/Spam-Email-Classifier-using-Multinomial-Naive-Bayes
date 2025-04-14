import pickle
import re
import string
import streamlit as st

# Load the trained model and vectorizer
with open("spam_classifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    return text

# Function to predict spam or not
def predict_spam(email_text):
    email_text = preprocess_text(email_text)
    email_tfidf = vectorizer.transform([email_text])
    prediction = model.predict(email_tfidf)
    return "Spam" if prediction[0] == 1 else "Not Spam"

# Streamlit UI
st.title("Spam Email Classifier")
st.write("Enter an email message below to check if it's spam or not.")

email = st.text_area("Enter your email message:")

if st.button("Check Spam Status"):
    if email:
        prediction = predict_spam(email)
        st.write(f"Prediction: **{prediction}**")
    else:
        st.write("Please enter an email message.")

# 📰 Fake News Detection System using Machine Learning & NLP

## 📌 Overview
Fake news has become a major challenge in the digital era, influencing public opinion and spreading misinformation at scale.  
This project presents an **end-to-end machine learning system** that classifies news articles as **Real** or **Fake** using Natural Language Processing (NLP) techniques and deploys the trained model as an interactive web application.

The focus of this project is not only model accuracy, but also **correct ML practices**, including data leakage prevention, proper evaluation, and deployment readiness.

---

## 🎯 Objectives
- Build a binary text classification model for fake news detection  
- Apply NLP techniques using a clean, leakage-free pipeline  
- Evaluate model stability using stratified cross-validation  
- Deploy the trained model with a user-friendly web interface  

---

## 🧠 Problem Type
- Supervised Learning  
- Binary Classification  
- NLP-based Text Classification  

---

## 📊 Dataset
**Source:** Fake News Detection Dataset (Kaggle)

### Files Used
- `True.csv` → Real news articles (label = 1)
- `Fake.csv` → Fake news articles (label = 0)


### Feature Selection
- `title` and `text` are combined into a single feature: **content**
- Metadata such as `subject` and `date` are excluded to avoid bias and leakage

---


## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, NLTK  
- **Modeling:** TF-IDF, Logistic Regression  
- **Deployment:** Streamlit  
- **Serialization:** Joblib  

## 👤 Author
**Aditya Sharma**  
Aspiring Machine Learning Engineer  

This project was built to demonstrate strong ML fundamentals, honest evaluation, and deployment readiness.

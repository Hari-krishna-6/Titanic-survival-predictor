# 🚢 Titanic Survival Prediction  

![Python](https://img.shields.io/badge/Python-3.9-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Deployed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview  
This project predicts whether a passenger survived the Titanic disaster using machine learning. It includes data preprocessing, exploratory data analysis (EDA), model building, and deployment using a web application.

---

## 🔗 Live Demo  
👉 https://huggingface.co/spaces/Hari-Krishna-06/titanic-survival-predictor 

---

## 📊 Dataset  
- Source: Kaggle Titanic Dataset  
- Rows: 891  
- Columns: 12  

---

## ⚙️ Data Preprocessing  

- Handled missing values:
  - Age → Median  
  - Embarked → Mode  
  - Cabin → Dropped  

- Removed unnecessary columns:
  - Name, Ticket, PassengerId  

- Encoded categorical features:
  - Sex → Label Encoding  
  - Embarked → One-hot Encoding  

---

## 📈 Exploratory Data Analysis  

Key insights:
- Sex is the strongest predictor of survival  
- Passenger class (Pclass) significantly affects survival  
- Females and 1st class passengers had higher survival rates  

---

## 🤖 Models Trained  

- Logistic Regression  
- Decision Tree  
- Random Forest  
- Bagging Classifier  

---

## 🏆 Best Model  

**Logistic Regression** was selected because:
- Lowest false negative rate  
- More reliable predictions  

---

## 📊 Results  

| Metric        | Value |
|--------------|------|
| Accuracy     | 77%  |
| AUC Score    | 0.84 |

---

## 💾 Model Saving  

- Model and scaler saved using Pickle  
- Enables fast predictions without retraining  

---

## 🌐 Web Application  

Built using Streamlit  

### Features:
- User input for passenger details  
- Instant survival prediction  
- Clean and simple interface  

---

## 🚀 Deployment  

- Deployed on Hugging Face Spaces  

---

## 🛠️ Tech Stack  

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Streamlit  
- Pickle  
- Git  


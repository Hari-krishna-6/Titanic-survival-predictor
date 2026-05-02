import streamlit as st
import pickle

st.title("Avan Polachanaa?")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
age = st.number_input("Age", min_value=0, max_value=100)

sex = st.selectbox("Sex", ["male", "female"])
if sex == "male":
    sex = 1
else:
    sex = 0

fare = st.number_input("Fare", min_value=0.0)
sibsp = st.number_input("Siblings/Spouses aboard", min_value=0, max_value=10)
parch = st.number_input("Parents/Children aboard", min_value=0, max_value=10)
embarked = st.selectbox("Embarked", ["C", "Q", "S"])
if embarked == "C":
    Embarked_C, Embarked_Q , Embarked_S = 1,0,0
elif embarked == "Q":
    Embarked_C , Embarked_Q , Embarked_S = 0,1,0
else:
    Embarked_C , Embarked_Q , Embarked_S = 0,0,1


with open("src/scale.pkl",'rb') as fh:
    scaler = pickle.load(fh)
with open("src/model.pkl","rb") as fh:
        model = pickle.load(fh)

if st.button("Predict"):

    input_row = [pclass,sex,age,sibsp,parch,fare, Embarked_C, Embarked_Q , Embarked_S]
    final_input = scaler.transform([input_row])
    x = model.predict(final_input)
    if x==1:
        st.write("Survived")
    else:
        st.write("Sethutaan")
import streamlit as st
import pickle

st.title("AI Disease Prediction System")

model = pickle.load(open("model.pkl","rb"))

fever = st.selectbox("Fever", [0,1])
cough = st.selectbox("Cough", [0,1])
headache = st.selectbox("Headache", [0,1])
vomiting = st.selectbox("Vomiting", [0,1])

if st.button("Predict"):
    prediction = model.predict([[fever,cough,headache,vomiting]])
    st.success("Predicted Disease: " + prediction[0])

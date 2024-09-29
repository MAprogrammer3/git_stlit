import streamlit as st
import joblib

st.title('Hello world')
model = joblib.load('linear.pkl')
 
st.write('##')
st.slider('')

x = st.slider('Experience' , 0, 40)
y = model.predict([[x]])
st.write('Salary is' , x)
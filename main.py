import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
# Streamlit app
st.title('Algorthmic Trading Model Prediction')

loaded_model = joblib.load('random_forest_model.pkl')

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    st.write(data.head())
    
    new_features = data[['RSI', 'k_percent', 'r_percent', 'Price_Rate_Of_Change', 'MACD', 'On Balance Volume']] 
    
    # # Make predictions
    predictions = loaded_model.predict(new_features)
    
    st.write(predictions)

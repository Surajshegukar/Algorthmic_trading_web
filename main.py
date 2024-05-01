import streamlit as st
import pandas as pd
import joblib as jl

# Load the pre-trained model
# Streamlit app
st.title('Algorthmic Trading Model Prediction')

loaded_model = jl.load("random_forest_model.pkl")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:")
    
    last_row = data[(data['datetime'] == data['datetime'].max())]
    st.write(last_row)
    
    new_features = last_row[['RSI', 'k_percent', 'r_percent', 'Price_Rate_Of_Change', 'MACD', 'On Balance Volume']]
    
    # # Make predictions
    predictions = loaded_model.predict(new_features)
    
    for i in range(len(predictions)):
        prediction = predictions[i]
        if str(prediction) == 1:
            st.write("Predicted Signal: Buy")
            st.write("the model is predicting a buy shares at the current price")
        else:
            st.write("Predicted Signal : Sell")
            st.write("the model is predicting a sell shares at the current price")
        
    

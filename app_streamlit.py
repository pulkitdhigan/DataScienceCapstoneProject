import pandas as pd
import numpy as np
import streamlit as st
from sklearn import *
import pickle

df = pd.read_csv('CAR Details.csv')
best_model = pickle.load(open('car_predict.pkl', 'rb'))

st.title('Car Selling Price Predictor')

st.header('Fill the details to predict the Car price')


# year 
year = st.selectbox('year', df['year'].unique())
# km 
km = st.selectbox('km driven', df['km_driven'].unique())
# fuel 
fuel = st.selectbox('fuel', df['fuel'].unique())
# seller
seller_type = st.selectbox('type seller', df['seller_type'].unique())
# transmission
transmission = st.selectbox('transmission', df['transmission'].unique())
# owner 
owner = st.selectbox('owner', df['owner'].unique())


if st.button('Predict Price') :
    test_data = np.array([year, km, fuel, seller_type, transmission, owner])
    test_data = test_data.reshape([1,6])

    st.success(best_model.predict(test_data)[0])
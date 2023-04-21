#pip install streamlit
import streamlit as st
import pandas as pd

import numpy as np

import pickle



# Load the data
data =pickle.load(open('df1.pkl','rb'))







			

features = ["km_driven", "fuel", "seller_type", "transmission", "owner", "year"]
target = "selling_price"

model=pickle.load(open('RF_Regression.pkl','rb'))
model.fit(data[features], data[target])

# Create the Streamlit app
st.title("Used Car Price Predictor")

# Get the user inputs

#km_driven = st.number_input("Kilometers Driven")
km_driven=st.slider('Select the distance the car has covered',0.0,300000.0)
fuel = st.selectbox("Fuel Type",['Petrol' ,'Diesel', 'CNG', 'LPG', 'Electric'])
seller_type= st.selectbox("seller_type",['Individual', 'Dealer' ,'Trustmark_Dealer'])
transmission = st.selectbox("Transmission",['Manual' ,'Automatic'])
owner = st.selectbox("Number of Owners",['First Owner', 'Second Owner' ,'Fourth & Above Owner' ,'Third Owner','Test_Drive_Car'])
#year = st.number_input("Number of Years")
#no_year=st.slider('Select the age of car',0.0,100.0)
year = st.selectbox('year', data['year'].unique())
#brand_name = st.selectbox('brand_name', data['brand_name'].unique())
#brand_name = st.selectbox('brand_name',['Maruti' ,'Hyundai' ,'Datsun' ,'Honda' ,'Tata' ,'Chevrolet' ,'Toyota' ,'Jaguar','Mercedes-Benz','Audi', 'Skoda' ,'Jeep' ,'BMW' ,'Mahindra' ,'Ford', 'Nissan','Renault' ,'Fiat' ,'Volkswagen' ,'Volvo' ,'Mitsubishi' ,'Land' ,'Daewoo', 'MG','Force' ,'Isuzu' ,'OpelCorsa', 'Ambassador' ,'Kia'])





if st.button('Predict car Price'):
    if fuel=="Petrol":
        fuel=4

    elif fuel=="Diesel":
        fuel=1
    elif fuel=="CNG":
        fuel=0
    elif fuel=='LPG':
        fuel=3
    elif fuel=='Electric':
        fuel=2
    if seller_type=="Individual":
        seller_type=1
    elif seller_type=="Dealer":
        seller_type=0
    elif seller_type=="Trustmark_Dealer":
        seller_type=2
    if transmission=="Manual":
        transmission=1
    elif transmission=="Automatic":
        transmission=0
    if owner=="First Owner":
        owner=0

    elif owner=="Second Owner":
        owner=2
    elif  owner=="Fourth & Above Owner":
        owner=1
    elif owner=="Third Owner":
        owner=4
    elif owner=="Test_Drive_Car":
        owner=3



   
    result = model.predict([[km_driven, fuel, seller_type, transmission, owner, year]])
    st.success("The estimated selling_price is ₹  {:,.0f}".format(result[0]))
   


#streamlit run app1.py

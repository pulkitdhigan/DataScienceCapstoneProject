#pip install streamlit
import streamlit as st
import pandas as pd

import numpy as np

import pickle



# Load the data
data =pickle.load(open('df1.pkl','rb'))







			

features = ["km_driven", "fuel", "seller_type", "transmission", "owner", "year" ,"brand_name"]
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
brand_name = st.selectbox('brand_name',['Maruti' ,'Hyundai' ,'Datsun' ,'Honda' ,'Tata' ,'Chevrolet' ,'Toyota' ,'Jaguar','Mercedes-Benz','Audi', 'Skoda' ,'Jeep' ,'BMW' ,'Mahindra' ,'Ford', 'Nissan','Renault' ,'Fiat' ,'Volkswagen' ,'Volvo' ,'Mitsubishi' ,'Land' ,'Daewoo', 'MG','Force' ,'Isuzu' ,'OpelCorsa', 'Ambassador' ,'Kia'])





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



    

    elif brand_name=="Maruti":
        brand_name=18
    elif  brand_name=="Hyundai":
        brand_name=10
    elif brand_name=="Datsun":
        brand_name=5
    elif brand_name=="Honda":
        brand_name=9
    elif brand_name=="Tata":
        brand_name=25
    elif  brand_name=="Chevrolet":
        brand_name=3
    elif brand_name=="Toyota":
        brand_name=26
    elif brand_name=="Jaguar":
        brand_name=12
    elif brand_name=="Mercedes-Benz":
        brand_name=19
    elif  brand_name=="Audi":
        brand_name=1
    elif brand_name=="Skoda":
        brand_name=24
    elif brand_name=="Jeep":
        brand_name=13
    elif brand_name=="BMW":
        brand_name=2
    elif  brand_name=="Mahindra":
        brand_name=17
    elif brand_name=="Ford":
        brand_name=8
    elif brand_name=="Nissan":
        brand_name=21
    elif brand_name=="Renault":
        brand_name=23
    elif  brand_name=="Fiat":
        brand_name=6
    elif brand_name=="Volkswagen":
        brand_name=27
    elif brand_name=="Volvo":
        brand_name=28
    elif brand_name=="Mitsubishi":
        brand_name=20
    elif  brand_name=="Land":
        brand_name=15
    elif brand_name=="Daewoo":
        brand_name=4
    elif brand_name=="MG":
        brand_name=16
    elif brand_name=="Force":
        brand_name=7
    elif  brand_name=="Isuzu":
        brand_name=11
    elif brand_name=="OpelCorsa":
        brand_name=22
    elif brand_name=="Kia":
        brand_name=14
    elif brand_name=="Ambassador":
        brand_name=0
   
    result = model.predict([[km_driven, fuel, seller_type, transmission, owner, year,brand_name]])
    st.success("The estimated selling_price is ₹  {:,.0f}".format(result[0]))
   


#streamlit run app.py

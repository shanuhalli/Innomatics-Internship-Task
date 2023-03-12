import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "mumbai_properties.csv")
JOBL_PATH = os.path.join(dir_of_interest, "data", "regression_model.joblib")

df = pd.read_csv(DATA_PATH)

joblib_in = open(JOBL_PATH,'rb')
reg = joblib.load(joblib_in)

def predict_price(Area_SqFt,Floor_No,Bedroom):
    x = np.zeros(7)
    
    x[0] = Area_SqFt
    x[1] = Floor_No
    x[2] = Bedroom

    return reg.predict([x])[0]

st.subheader('Please enter the required details :')
Location = st.selectbox('Select the Location',(df['Region'].sort_values().unique()))
Area_SqFt = st.slider("Select Total Area in SqFt",500,int(max(df['Area_SqFt'])),step=100)    
Floor_No = st.selectbox("Enter Floor Number",(df['Floor_No'].sort_values().unique()))
Bathroom = st.selectbox("Enter Number of Bathroom",(df['Bathroom'].sort_values().unique()))
Bedroom = st.selectbox("Enter Number of Bedroom",(df['Bedroom'].sort_values().unique()))
Property_Age = st.selectbox('Select the Property Age',(df['Property_Age'].sort_values().unique()))
result= ""

if st.button("Calculate Price"):
    result = predict_price(Area_SqFt,Floor_No,Bedroom)
st.success('Total Price in Lakhs : {}'.format(result))
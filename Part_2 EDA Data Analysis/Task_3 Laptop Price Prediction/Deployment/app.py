import joblib
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="wide")

st.title("Laptop Price Predictor 💻")
st.subheader( "All the fields are mandatory")
df = pd.read_csv('laptop_data.csv')
model = joblib.load('rf_model.pkl')

# making 2 cols left_column and right_column
left_column, right_column = st.columns(2)
with left_column:
    ops = st.selectbox("Operating System", options=df["OS"].sort_values().unique())
    def operating_system(ops):
        if ops == "Windows 11":
            return 4
        elif ops == "Windows 10":
            return 3
        elif ops == "Mac OS":
            return 2
        elif ops == "DOS":
            return 1
        elif ops == "Chrome":
            return 0
    laptop_os = operating_system(ops)

with right_column:
    generation = st.selectbox("Generation", options=df["Generation"].sort_values().unique())
    def gen_lap(generation):
        if generation == "11th Gen":
            return 1
        elif generation == "10th Gen":
            return 0
        elif generation == "Undefine":
            return 5
        elif generation == "12th Gen":
            return 2
        elif generation == "9th Gen":
            return 4
        elif generation == "8th Gen":
            return 3
    laptop_gen = gen_lap(generation)

# making 2 cols left_column and right_column
left_column, right_column = st.columns(2)
with left_column:
    processor = st.selectbox("Processor Name",options=df["Processor"].sort_values().unique())
    def pro_name(processor):
        if processor == "Intel Core i3 Processor":
            return 17
        elif processor == "AMD Ryzen 5 Hexa Core Processor":
            return 6
        elif processor == "Intel Core i5 Processor":
            return 18
        elif processor == "AMD Ryzen 7 Quad Core Processor":
            return 9
        elif processor == "AMD Ryzen 5 Quad Core Processor":
            return 7
        if processor == "AMD Ryzen 9 Octa Core Processor":
            return 10
        elif processor == "AMD Ryzen 7 Octa Core Processor":
            return 8
        elif processor == "Apple M1 Processor":
            return 13
        if processor == "Intel Celeron Dual Core Processor":
            return 15
        elif processor == "AMD Ryzen 3 Dual Core Processor":
            return 2
        elif processor == "AMD Athlon Dual Core Processor":
            return 0
        if processor == "Intel Evo Core i5 Processor":
            return 21
        elif processor == "AMD Ryzen 3 Quad Core Processor":
            return 4
        elif processor == "Apple M2 Processor":
            return 14
        if processor == "Intel Celeron Quad Core Processor":
            return 16
        elif processor == "Intel Core i7 Processor":
            return 19
        elif processor == "Apple M1 Pro Processor":
            return 12
        elif processor == "Intel Pentium Silver Processor":
            return 23
        elif processor == "Apple M1 Max Processor":
            return 11
        elif processor == "Intel Core i9 Processor":
            return 20
        elif processor == "AMD Ryzen 5 Dual Core Processor":
            return 5
        elif processor == "Intel Pentium Quad Core Processor":
            return 22
        elif processor == "AMD Dual Core Processor":
            return 1
        elif processor == "AMD Ryzen 3 Hexa Core Processor":
            return 3
    processor_name = pro_name(processor)

with right_column:
    display_cm = st.selectbox('Dispaly in centimeters', ['29.46', '33.78', '35.56', '39.62', '40.64', '43.94'])

# making 2 cols left_column and right_column
left_column, right_column = st.columns(2)
with left_column:
    ram_type = st.selectbox("RAM Type",options=df["RAM_Type"].sort_values().unique())
    def ram_name(ram_type):
        if ram_type == "DDR4":
            return 0
        elif ram_type == "DDR5":
            return 1
        elif ram_type == "RAMMac":
            return 4
        elif ram_type == "LPDDR4X":
            return 3
        elif ram_type == "LPDDR3":
            return 2
    type_of_ram = ram_name(ram_type)

with right_column:
    ram_in_gb = st.selectbox('RAM in GB', ['4', '8', '16', '32'])

# making 2 cols left_column and right_column
left_column, right_column = st.columns(2)
with left_column:
    ssd_in_gb = st.selectbox('SSD in GB', options=df["SSD"].sort_values().unique())

with right_column:
    hdd_in_gb = st.selectbox('HDD in GB', options=df["HDD"].sort_values().unique())


features = [[laptop_os,laptop_gen,processor_name,type_of_ram,ram_in_gb,ssd_in_gb,hdd_in_gb,display_cm]]
final_features = np.array(features).reshape(1, -1)

if st.button('Predict Price'):
    prediction = model.predict(final_features)
    st.balloons()
    st.success(f'### Laptop Predicted Price is Rs. {int(prediction[0])} ₹')
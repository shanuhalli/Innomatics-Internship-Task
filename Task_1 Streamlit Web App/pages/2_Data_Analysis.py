import os
import pandas as pd
from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "mumbai_properties.csv")
IMG1_PATH = os.path.join(dir_of_interest, "images", "Real_Estate.jpg")
IMG2_PATH = os.path.join(dir_of_interest, "images", "Price_Range_Distribution.png")
IMG3_PATH = os.path.join(dir_of_interest, "images", "Central Mumbai.png")
IMG4_PATH = os.path.join(dir_of_interest, "images", "South Mumbai.png")

st.subheader("Real Estate : Data Analysis")

submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
df = pd.read_csv(DATA_PATH)

if submenu == "Descriptive":
	img1 = Image.open(IMG1_PATH)
	st.image(img1)
	
	with st.expander("Dataset"):
		st.dataframe(df)

	with st.expander("Data Types"):
		st.dataframe(df.dtypes)

	with st.expander("Data Summary"):
		st.dataframe(df.describe())

	with st.expander("Location Distribution"):
		st.dataframe(df["Region"].value_counts().head(30))

elif submenu == "Plots":
	with st.expander("Price with respect to Location"):
		st.bar_chart(data=df, x="Region", y="Price_Lakh", width=300, height=500, use_container_width=True)

	with st.expander("Price with respect to Floor"):
		st.bar_chart(data=df, x="Floor_No", y="Price_Lakh", width=300, height=500, use_container_width=True)
	
	with st.expander("Price with respect to Total Area"):
		st.bar_chart(data=df, x="Area_SqFt", y="Price_Lakh", width=300, height=500, use_container_width=True)

	with st.expander("Distribution : Age of Property"):
		labels = '1 to 5 Year','0 to 1 Year','5 to 10 Year','10+ Year','Under Construction'
		explode = [0.005,0.005,0.005,0.005,0.005]  # only "explode" the 2nd slice (i.e. 'Hogs')

		fig1, ax1 = plt.subplots()
		ax1.pie(df['Property_Age'].value_counts(), explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
		ax1.axis('equal')  
		st.pyplot(fig1)

	with st.expander("Distribution : Price Range"):
		img2 = Image.open(IMG2_PATH)
		st.image(img2)
	
	with st.expander("Central Mumbai Property Price"):
		img3 = Image.open(IMG3_PATH)
		st.image(img3)

	with st.expander("South Mumbai Property Price"):
		img4 = Image.open(IMG4_PATH)
		st.image(img4)
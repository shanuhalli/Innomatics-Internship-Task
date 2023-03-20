import os
from PIL import Image
import streamlit as st
import streamlit.components.v1 as stc

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

HTML_PATH = os.path.join(dir_of_interest, "images", "mumbai_property.html")
IMG_PATH = os.path.join(dir_of_interest, "images", "Realty_Growth.jpg")

html_temp = """
			<div style="background-color:#8A9A5B;padding:10px;border-radius:10px">
			<h1 style="color:white;text-align:center;"> Real Estate Price Prediction</h1>
			<h3 style="color:white;text-align:center;"> Presented by : Shanu Halli </h3>
			</div>
			"""
def main():
	stc.html(html_temp)

	menu = ["About", "Property Location"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="About":
		img1 = Image.open(IMG_PATH)
		st.image(img1)
		st.write("""
				## `Thinking Ahead`
				Real estate prices are deeply cyclical and much of it is dependent on factors you can't control.
				Whether you plan on buying a new property or want to use the equity in your home for other expenses,
				it is important to analyze both broader market conditions and your specific property
				to determine how the home's value may fare over the course of time.
				
				## `Real Estate Price Prediction ML App`
				##### 1. This App predict the price of property.
				##### 2. Estimate your budget as per your requirements.
				""")
	else:
		path_to_html = (HTML_PATH)

		with open(path_to_html,'r') as f: 
			html_data = f.read()

		st.subheader("Data points which is working on the project :")
		st.components.v1.html(html_data,height=500)

main()
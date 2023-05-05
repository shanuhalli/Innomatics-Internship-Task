import folium
import pandas as pd
from PIL import Image
import streamlit as st
#st.set_page_config(layout="wide")

# Load the dataset
data = pd.read_csv('data\clean_pub_data.csv')
image = Image.open("data\pub_image.jpg")

total_pubs = len(data)
postcodes = len(data['PostCode'].unique())
local_authorities = len(data['Local_Authority'].unique())

# Create the Home Page
def home_page():
    st.markdown("<h1 style='color: red'>Welcome to the Pub Finder App</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: blue'>Find pubs near you based on your Location</h2>", unsafe_allow_html=True)
    st.image(image, width= 750)
    st.write('### :green[Total number of pubs in the dataset:]', total_pubs)
    st.write('### :green[Number of unique postcodes in the dataset:]', postcodes)
    st.write('### :green[Number of unique local authorities in the dataset:]', local_authorities)

# Run the app
if __name__ == '__main__':
    home_page()
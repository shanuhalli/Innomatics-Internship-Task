import folium
import pandas as pd
import streamlit as st
import scipy.spatial.distance as dist
from streamlit_folium import folium_static

# Load the dataset
df = pd.read_csv('data\clean_pub_data.csv')

# Create the Nearest Pub Page
def nearest_pub():
    st.markdown("<h1 style='color: red'>Find the Nearest Pub</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        user_lat = st.number_input(label="Enter Latitude Here", min_value=49.8924, max_value=60.7649)
    with col2:
        user_lon = st.number_input(label="Enter Longitude Here", min_value=-7.3845, max_value=1.7577)

    # Calculate Distance
    df["Distance"] = df.apply(lambda row: dist.euclidean((user_lat, user_lon), (row["Latitude"], row["Longitude"])), axis=1)

    # Get 5 Nearest Pubs
    nearest_pubs = df.sort_values(by=["Distance"]).head(5)

    st.markdown("<h3 style='color: green'>Nearest Pub List</h3>", unsafe_allow_html=True)
    st.write(nearest_pubs[["Name", "Address", "PostCode", "Local_Authority", "Distance"]])

    st.markdown("<h3 style='color: green'>Nearest Pub on Map</h3>", unsafe_allow_html=True)
    maps = folium.Map(location=[user_lat, user_lon], zoom_start=10)
    folium.Marker(location=[user_lat, user_lon], icon=folium.Icon(icon='star', color='red'), popup='Your Location').add_to(maps)

    for index, row in nearest_pubs.iterrows():
        iframe = folium.IFrame('Name : ' + str(row.loc['Name']) + '<br>' + 
                               'Address : ' + str(row.loc['Address']) + '<br>' + 
                               'PostCode : ' + str(row.loc['PostCode']))
        popup = folium.Popup(iframe, min_width=200, max_width=250)
        folium.Marker(location=[row['Latitude'], row['Longitude']], popup=popup).add_to(maps)
    folium_static(maps)

# Run the app
if __name__ == '__main__':
    nearest_pub()
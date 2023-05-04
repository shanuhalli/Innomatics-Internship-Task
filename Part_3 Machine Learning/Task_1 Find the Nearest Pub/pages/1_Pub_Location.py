import folium
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static

# Load the dataset
data = pd.read_csv('data\clean_pub_data.csv')

# Create the Pub Locations Page
def location_page():
    st.markdown("<h1 style='color: red'>Pub Locations</h1>", unsafe_allow_html=True)
    st.write("<h2 style='color: blue'>Enter the Postal Code or Local Authority to find pubs in the area</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        searchType = st.selectbox('Search by', ('Local Authority', 'Postal Code'))
    
    with col2:
        if searchType == 'Local Authority':
            localAuthority = st.selectbox('Enter the Local Authority', options= data["Local_Authority"].sort_values().unique())
            pubs = data[data['Local_Authority'] == localAuthority]
        else:
            postCode = st.selectbox('Enter the Postal Code', options= data["PostCode"].sort_values().unique())
            pubs = data[data['PostCode'] == postCode]
    
    # Display the map
    st.markdown("<h3 style='color: green'>Pubs on Map</h3>", unsafe_allow_html=True)
    if len(pubs) > 0:
        maps = folium.Map(location=[pubs['Latitude'].mean(),pubs['Longitude'].mean()], zoom_start=10)
        for index, row in pubs.iterrows():
            iframe = folium.IFrame('Name : ' + str(row.loc['Name']) + '<br>' + 
                                   'Address : ' + str(row.loc['Address']) + '<br>' + 
                                   'PostCode : ' + str(row.loc['PostCode']))
            popup = folium.Popup(iframe, min_width=200, max_width=250)
            folium.Marker(location=[row['Latitude'], row['Longitude']], popup=popup).add_to(maps)
        folium_static(maps)

# Run the app
if __name__ == '__main__':
    location_page()
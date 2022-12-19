"""
Name: Remi LeSage
Final Project
Description: This program allows users to interact with a site about all the skyscrapers in the world.
"""
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import pydeck as pdk
from PIL import Image

# Setting text color for sidebar success text
st.markdown('''
<style>
.st-b7 {
    color: Blue;
}
.sidebar .sidebar-content {
    color: Blue;
}
.css-nlntq9 {
    font-family: Source Sans Pro;
}
</style>
''', unsafe_allow_html=True)

# Heading
st.title("Skyscrapers in the World")
st.write("Explore this site to learn more about the 99 tallest skyscrapers in the world!")
image = Image.open("tallestbuildings.jpg")
st.image(image, caption = 'Shanghai Tower, Lotte World Tower, Burj Khalifa, Taipei 101, International Commerce Center, One World Trade Center, Abraj Al-Bait Clock Tower, CTF Finance Center', width = 750)

# Create a sidebar
st.sidebar.header("Interact with the prompts below to learn more!")

# Query #1 --> Charts comparing floors of different buildings in ranks of heights.
# Allowing users to select whether they want to see a bar chart, scatter plot, or simple line plot through a drop-down menu.
st.sidebar.success("Below you can select what chart you would like to see to be able to view the number of floors for all 99 skyscrapers. They are ranked in order of height. You will see that height doesn't play a huge factor in how many floors a building has.")
selected_chart = st.sidebar.selectbox("Please select the chart you want to see: ", ["", "Bar Chart", "Scatter Plot", "Simple Line Plot"])
path = "C:/Users/Remi/OneDrive/CS 230/Final Project/"
df = pd.read_csv(path + "Skyscrapers2021.csv")
x = df['RANK']
y = df['FLOORS']

if selected_chart == "Bar Chart":
    selected_color = st.sidebar.radio("Please select the bar color:", ["red", "orange", "yellow", "green", "blue", "magenta"])
    fig, ax = plt.subplots()
    ax.bar(x, y, color = selected_color)
    fig.text(0.5, 0.04, 'Rank', ha='center', va='center')
    fig.text(0.03, 0.5, 'Floors', ha='center', va='center', rotation='vertical')
    ax.set_title('Bar Chart')
    st.pyplot(fig)

elif selected_chart == "Scatter Plot":
    selected_color1 = st.sidebar.radio("Please select the scatter plot color:", ["red", "orange", "yellow", "green", "blue", "magenta"])
    selected_marker = st.sidebar.radio("Please select the marker style:", [".", "o", "x", "D", "H", "s", "+"])
    fig1, ax1 = plt.subplots()
    ax1.scatter(x, y, color = selected_color1, marker = selected_marker)
    fig1.text(0.5, 0.04, 'Rank', ha='center', va='center')
    fig1.text(0.03, 0.5, 'Floors', ha='center', va='center', rotation='vertical')
    ax1.set_title('Scatter Plot')
    st.pyplot(fig1)

elif selected_chart == "Simple Line Plot":
    selected_color2 = st.sidebar.radio("Please select the line color:", ["red", "orange", "yellow", "green", "blue", "magenta"])
    selected_line = st.sidebar.radio("Please select the line style:", ["-", "--", "-.", ":"])
    fig2, ax2 = plt.subplots()
    ax2.plot(x, y, color = selected_color2, linestyle = selected_line)
    fig2.text(0.5, 0.04, 'Rank', ha='center', va='center')
    fig2.text(0.03, 0.5, 'Floors', ha='center', va='center', rotation='vertical')
    ax2.set_title('Simple Line Plot')
    st.pyplot(fig2)

# Query #2 --> Slider to select a year and show skyscrapers completed in that year
st.sidebar.success("Next you can select a year in between 2000-2020. Once the year is selected, you will be able to view a complete list of the skyscrapers created during that year!")

def year_name(year):
    st.write(f"The year you selected is {year}.")
    name_data = df[(df['COMPLETION'] == year)].set_index('NAME')
    name_data.sort_values(["NAME"], ascending = [True], inplace = True)
    st.write(name_data)

# Query #3 --> Showing a map with all the skyscrapers on it.
def view_map():
    st.write(f"Zoom in to see where/what skyscrapers are in a city! ")
    path = "C:/Users/Remi/OneDrive/CS 230/Final Project/"
    df = pd.read_csv(path + "Skyscrapers2021.csv")
    Skyscraper_names = []
    for name in df['NAME']:
        Skyscraper_names.append(name)
    Longitude = []
    for longitude in df['Longitude']:
        Longitude.append(longitude)
    Latitude = []
    for latitude in df['Latitude']:
        Latitude.append(latitude)

    LOCATION = list(zip(Skyscraper_names,Latitude,Longitude))

    df = pd.DataFrame(LOCATION,columns=["Building Name", "lat", "lon"])

    view_state = pdk.ViewState(
        latitude=df["lat"].mean(),
        longitude=df["lon"].mean(),
        zoom = 3,
        pitch = 0)

    layer_1 = pdk.Layer('ScatterplotLayer',
                      data = df,
                      get_position = '[lon, lat]',
                      get_radius = 200,
                      get_color = [255,0,255],
                      pickable = True)

    tool_tip = {"html": "Building Name:<br/> <b>{Building Name}</b>",
                "style": { "backgroundColor": "steelblue",
                            "color": "white"}}
    map = pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v12',
        initial_view_state=view_state,
        layers=[layer_1],
        tooltip= tool_tip
    )
    st.pydeck_chart(map)

def main():
    year_name(year = st.sidebar.slider(f"Please select a year:", min_value = 2000, max_value = 2020))
    view_map()
main()

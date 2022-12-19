"""
Name: Remi LeSage
"""

import pandas as pd
import streamlit as st
from PIL import Image

# Title and image
st.title("Facts About the 99 Tallest Skyscrapers!")
image = Image.open("BurjKhalifa.jpg")
st.image(image, width = 500)

# Setting color and font for st.success titles
st.markdown('''
<style>
.st-b7 {
    color: Blue;
}
.css-nlntq9 {
    font-family: Source Sans Pro;
}
</style>
''', unsafe_allow_html=True)

# Quiz with Text Box
def quiz(skyscraper_name = 'Burj Khalifa'):
    st.write("Quiz Time: What is the tallest skyscraper in the world?")
    user_answer = st.text_input("Skyscraper Name: ", "").lower()
    if user_answer == skyscraper_name.lower():
        st.write(f"You are correct!")
        st.balloons()
    elif user_answer == "":
        pass
    else:
        st.write(f"That's incorrect! The tallest skyscraper is Burj Khalifa!")
quiz()

# Query 5 --> Group dataframe showing how many skyscrapers are in each state
df = pd.read_csv("Skyscrapers2021.csv")
df1 = pd.DataFrame(df)
st.success("Pivot Table That Shows the Number of Skyscrapers in Each City")
df1_g2 = df1.groupby(by = ["CITY"]).nunique()
st.write(df1_g2['NAME'])

# Query #4 --> Data frame with top 10 skyscrapers and links to learn more.
st.success("Click on the Links Below to See More About the 10 Tallest Skyscrapers in the World!")
for row in df.itertuples():
        if row.RANK <= 10:
            st.write(row.RANK, row.NAME, row.Link)

# Query #6 --> Data frame that shows all data with some columns dropped
st.success("All 99 Skyscrapers with Information About Rank, Name, City, Address, Feet, Floors, Material, Function, and a Link to Learn More")
df_data = pd.DataFrame(df)
df_data.drop(["Latitude", "Longitude", "Height", "Meters"], axis = 1, inplace = True)
st.write(df_data)


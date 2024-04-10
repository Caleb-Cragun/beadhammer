import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Welcome to Beadhammer!")

col1, col2 = st.columns(2)

with col1:
    st.image("images/beadhammer.jpg")
    st.title("Why Perler Beads?")
    why_content = """
      When I was introduced to the hobby, I didn't have a lot of extra funds to spend on getting models. However, I did have a ton of extra perler beads (and quite a bit of extra time). So, putting my time and beads to work, I made a custom army for wargaming in the Grimdark Future. For in the grim darkness of the far flung future, there is only beads...and war.
    """
    st.info(why_content)


with col2:
    st.title("What is BeadHammer?")
    about_content = """
      BeadHammer is a site featuring creations made of perler beads used as stand-ins for Warhammer 40k models. 
    """
    st.info(about_content)
    st.title("What can you expect to find?")
    find_content = """
      Here, I'll feature models that I've put together using ideas and designs that I've found on pinterest, as well as some self made designs. Also, I'll have a guide on making the comparable size bases for your models.
    """
    st.info(find_content)

st.title("Gallery")
st.write("Here's a few of the models I've made.")

df = pd.read_csv("data.csv", sep=",")

col3, col4 = st.columns(2)

with col3:
  for index, row in df[:5].iterrows():
    st.header(row["name"])
    st.subheader(row["faction"])
    st.image('images/' + row["image"])
    st.write(row["description"])

with col4:
  for index, row in df[5:].iterrows():
    st.header(row["name"])
    st.subheader(row["faction"])
    st.image('images/' + row["image"])
    st.write(row["description"])
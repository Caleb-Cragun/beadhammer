import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/beadhammer.jpg")

with col2:
    st.title("Beadhammer")
    content = """
      BeadHammer is a site featuring creations made of perler beads used as stand-ins for Warhammer 40k models. 
    """
    st.info(content)

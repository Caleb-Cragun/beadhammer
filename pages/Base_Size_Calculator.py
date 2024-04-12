import streamlit as st

st.set_page_config(layout="wide")
st.title("Base Size Calculator")
calculator_info = """
  This is a simple calculator to determine how many beads you'll need to make a base for your model. 
  I've discovered a bit of a pattern in determining the number of beads needed for a base. This calculator
  will take the size of the base in millimeters and convert it to the diamater of beads needed for a round base,
  or to the length and width of beads needed for an oval base. Once you have the dimensions, I recommend using
  a [Minecraft Circle Generator](https://donatstudios.com/PixelCircleGenerator) to get the pattern for the base.
  This generator is particulary good since it also does ovals.
"""
st.info(calculator_info)   

if st.checkbox('Oval?'):
  width = st.text_input(label='Width (mm)', key='oval_width')
else:
   width = None

length = st.text_input(label='Length (mm)', key='oval_length')

def convert_mm_to_beads():
    l = int(length)
    w = int(width) if width else None
    result = {}
    if l:
      result['length'] = l // 5 + 1    
    if w:
      result['width'] = w // 5 + 1
    if l < 10 or (w and w < 10):
      result['message'] = "This is too small for a stable base."
    if l >= 130 or (w and w >= 130):
      result['message'] = "This is too big for a single pegboard plate."
    return result


if st.button('Calculate'):
    result = convert_mm_to_beads()
    if 'width' in result:
      st.write(f"Width: {result['width']} beads")
    st.write(f"Length: {result['length']} beads")
    if 'message' in result:
      st.write(result['message'])
    
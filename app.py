# credit https://www.youtube.com/watch?v=VqgUkExPvLY
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title='Cameron Wolff Portfolio, Developer', page_icon='🛰', layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- LOAD ASSETS ---
lottie_coding = load_lottieurl('https://assets5.lottiefiles.com/private_files/lf30_ifzxw6ej.json')
img = Image.open('image/hunter.png')


# --- HEADER SECTION ---
with st.container():
    st.subheader('Hi, I am Cameron Wolff :wave:')
    st.title('A Computer Science student studying at Cal Poly SLO')
    st.write('I am passionate about building robots and data science')
    st.write('[Github >](https://github.com/camwolff02)')
    st.write('[Linkedin >](https://www.linkedin.com/in/cameron-wolff-83ba55218/)')

# --- WHAT I DO ---
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What I do')
        st.write('##')
        st.write(
            """
            About me:
            - Thing number one
            - Thing number two
            - Thing number three
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')

# --- PROJECTS ---
st.write('---')
st.header('My Projects')
st.write('##')

with st.container():  # Project 1
    image_column, text_column = st.columns((1, 2))  # 1:2 ratio
    
    with image_column:
        st.image(img)

    with text_column:
        st.subheader('Project name')
        st.write(
            """
            project description
            """
        )
        st.markdown('[link](https://www.youtube.com/watch?v=VqgUkExPvLY)')

with st.container():  # Project 2
    image_column, text_column = st.columns((1, 2))  # 1:2 ratio
    
    with image_column:
        st.image(img)

    with text_column:
        st.subheader('Project name')
        st.write(
            """
            project description
            """
        )
        st.markdown('[link](https://www.youtube.com/watch?v=VqgUkExPvLY)')

"""
Methods on home page.
"""

#Import Libraries
import streamlit as st
from PIL import Image
from image import user_input
from audio import user_input_audio
from streamlit_extras.stylable_container import stylable_container


def correct_grammar():

    st.markdown("<h1 style='text-align: center; color: #6699CC;'>Grammar Correction Tool</h1>", unsafe_allow_html=True)

    st.markdown("""
    <style>
        .divider {
            border-left: 2px solid #f0f0f0;
            height: 300px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Create columns with specific widths
    file_uploader_column, divider, output_column = st.columns([5.5, 0.1, 5])

    with file_uploader_column:
        uploaded_image = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"], key="file_uploader_image")
        uploaded_audio = st.file_uploader("Upload an audio file", type=["wav"], key="file_uploader_audio")

    with divider:
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    with output_column:
        if uploaded_image is not None:
            with st.container(height=300, border=True):
                st.write("")
                image = Image.open(uploaded_image)
                output_image = user_input(image)
                with stylable_container("codeblock","""code {white-space:
                                            pre-wrap !important;}""",):
                    st.code(output_image)
        elif uploaded_audio is not None:
            with st.container(height=300, border=True):
                st.write("")
                output_audio = user_input_audio(uploaded_audio)
                with stylable_container("codeblock","""code {white-space:
                                            pre-wrap !important;}""",):
                    st.code(output_audio)





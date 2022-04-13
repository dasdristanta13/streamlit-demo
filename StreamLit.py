from cv2 import resize
import streamlit as st
import numpy as np
from pandas import DataFrame
from streamlit_cropper import st_cropper
from PIL import Image
import seaborn as sns
# For download buttons
from functionforDownloadButtons import download_button
import os
import json

st.set_page_config(
    page_title="Licence Plate Detector",
    page_icon="🚌",
)


def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


_max_width_()

c30, c31, c32 = st.columns([2.5, 1, 3])

with c30:
    # st.image("Logo1.png", width=400)
    st.title("🚌 Licence Plate Detector")
    st.header("")



with st.expander("ℹ️ - About this app", expanded=True):

    st.write(
        """     
-   This app is a demo of a licence plate detector.
-   It is work of an academic project.
	    """
    )

    st.markdown("")

st.markdown("")
st.markdown("## **📌 Paste document **")
cropped_img=True
with st.form(key="my_form"):


    ce, c1, ce, c2, c3 = st.columns([0.07, 2, 0.07, 5, 0.07])
    with c1:

        st.markdown("Input Image")
        img_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
        realtime_update = st.checkbox(label="Update in Real Time", value=True)
        box_color = st.color_picker(label="Box Color", value='#00F2FF')
        aspect_choice = st.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
        aspect_dict = {
            "1:1": (1, 1),
            "16:9": (16, 9),
            "4:3": (4, 3),
            "2:3": (2, 3),
            "Free": None
        }
        aspect_ratio = aspect_dict[aspect_choice]
        submit_button1 = st.form_submit_button(label="✨ Get me the Image!")
    with c2:
        

        if img_file:
            img = Image.open(img_file)
            if not realtime_update:
                st.write("Double click to save crop")
            
            # if submit_button:
                # Get a cropped image from the frontend
            cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                                        aspect_ratio=aspect_ratio)

                # Manipulate cropped image at will
            st.write("Preview")
            _ = cropped_img.thumbnail((150,150))
        if cropped_img:
            submit_button = st.form_submit_button(label="✨ Get me the data!")




st.markdown("## **🎈 Check results **")

st.header("")

# cs, c1, c2, c3, cLast = st.columns([4, 1.5, 1.5, 1.5, 2])

st.markdown("")
# with cs:
if submit_button:
    hw=[i*3 for i in list(cropped_img.size)]
    st.image(cropped_img.resize((hw[0],hw[1])))


st.header("")



c1, c2, c3 = st.columns([1, 3, 1])

format_dictionary = {
    "Relevancy": "{:.1%}",
}


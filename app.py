import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
from PIL import Image

"""
### Created By : Bala Murugan
#### LinkedIn : https://www.linkedin.com/in/balamurugan14/

# Binary Image Classification
"""
model = tf.keras.models.load_model("model.h5")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    #bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    image = Image.open(uploaded_file)
    img = image.resize((224,224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0) # [batch_size, row, col, channel]
    result = model.predict(img_array) # [[0.99, 0.01], [0.99, 0.01]]

    argmax_index = np.argmax(result, axis=1) # [0, 0]
    st.header('PREDICTED OUTPUT', divider='rainbow')
    if argmax_index[0] == 0:
        st.image(image)
        st.header('\t :blue[CAT]')
    else:
        st.image(image)
        st.header('\t :red[DOG]')
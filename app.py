# -*- coding: utf-8 -*-
"""app_py1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1urlf8ldacsZs6ikRfh6bSYBW2ri_lB7s
"""

%%writefile app.py
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2

Load the pre-trained model
model = tf.keras.models.load_model("/content/model - 32x64 bs_1024 ep_5 acc_0.871 loss_0.345  (1).h5")
# Load the characters list
class_idx = ['0','1','2','3','4','5','6','7','8','9',
              'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 
 def predict_character(image):
     # Convert the image to grayscale
     gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
 
     # Resize the image to match model input shape
     resized_image = cv2.resize(gray_image, (28, 28))
 
     # Invert the colors
     inverted_image = cv2.bitwise_not(resized_image)
 
     # Add channel dimension
     input_image = np.expand_dims(inverted_image, axis=-1)
     input_image = np.expand_dims(input_image, axis=0)
 
     # Predict the image
     scores = model.predict(input_image)
 
     # Get the predicted character index
     index = np.argmax(scores)
 
     # Return the predicted character
     return class_idx[index]
 
 def apply_style(predicted_char, font_size=60):
     # Set the font
     font_path = "/content/RowlandDemoCaligraphy.ttf"  # Path to a font file
     font = ImageFont.truetype(font_path, size=font_size)
 
     # Create a blank image with white background
     img = Image.new('RGB', (100, 100), color=(255, 255, 255))
 
     # Draw the predicted letter on the image
     draw = ImageDraw.Draw(img)
 
     # Calculate text size and position for centering
     text_width, text_height = draw.textsize(predicted_char, font=font)
     text_x = (100 - text_width) // 2
     text_y = (100 - text_height) // 2
 
     draw.text((text_x, text_y), predicted_char, fill=(0, 0, 0), font=font)
 
     return img
 
# Streamlit app
 st.title("Character Recognition App")
 
# Upload image
uploaded_file = st.file_uploader("Upload an image from x_test dataset", type=["jpg", "png", "jpeg"])
 
# Check if predict button is clicked
if uploaded_file is not None:
     # Open and display the uploaded image
     pil_image = Image.open(uploaded_file)
 
     # Resize uploaded image to a fixed size
     fixed_size = (200, 200)
     pil_image = pil_image.resize(fixed_size)
 
     st.image(pil_image, caption='Uploaded Image (Fixed Size)', use_column_width=False, width=fixed_size[0])
 
     # Check if predict button is clicked
     if st.button("Predict"):
         # Convert image to numpy array
         image = np.array(pil_image)
 
         # Predict the character
         predicted_char = predict_character(image)
 
         # Display the predicted character
         st.write("Predicted Character:", predicted_char)
 
         # Apply style to the predicted letter
         styled_img = apply_style(predicted_char)
 
         # Display the styled image
         st.image(styled_img, caption='Styled Predicted Letter', use_column_width=False)

"""## Run app.py File by following command"""

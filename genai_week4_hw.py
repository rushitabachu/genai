# -*- coding: utf-8 -*-
"""GENAI_Week4_HW.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DB9coySPPwUnqa4uCx1-s3VYYiA7ehVT
"""

! pip install streamlit -q

!wget -q -O - ipv4.icanhazip.com

!pip install happytransformer

# Commented out IPython magic to ensure Python compatibility.
%%writefile app.py
import streamlit as st
from happytransformer import HappyTextToText, TTSettings

happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
args = TTSettings(num_beams=5, min_length=1)

#title
st.title("Grammar Corrector")

#Text input
user_input = st.text_area("Enter a sentence to correct grammatical errors:")

#Button text
 if st.button("Correct Grammar"):
     if user_input:
         # Add the prefix "grammar: " before the input text
         result = happy_tt.generate_text(f"grammar: {user_input}", args=args)
 
        #Output
         st.write("Corrected Sentence:")
         st.write(result.text)
     else:
         st.write("Enter a sentence")


!streamlit run app.py & npx localtunnel --port 8501

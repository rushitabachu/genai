# -*- coding: utf-8 -*-
"""app_code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oH18cNmbgG13xqpwrbz4pnJvgfzclQ2X
"""

import streamlit as st
from happytransformer import HappyTextToText, TTSettings

happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
args = TTSettings(num_beams=5, min_length=1)

#title
st.title("Grammar Corrector")

# Text input
input = st.text_area("Enter a sentence to correct grammatical errors:")

#Button text
if st.button("Correct Grammar"):
    if input:
        # Add the prefix "grammar: " before the input text
        output = happy_tt.generate_text(f"grammar: {input}", args=args)

        #Output
        st.write("Corrected Sentence:")
        st.write(output.text)
    else:
        st.write("Enter a sentence")
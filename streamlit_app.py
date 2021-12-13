import streamlit as st
import numpy as np
import tensorflow as tf
import tensorflow_text as tf_text

st.title("English-to-Spanish Translation App")

input_text = st.text_area("Enter text in English:")
input_text = tf.constant([input_text])

loaded_translator = tf.saved_model.load("translator")
raw_translated_text = loaded_translator.tf_translate(input_text = input_text)
translated_text = raw_translated_text["text"][0].numpy().decode()
trimmed_translated_text = translated_text[:len(translated_text) - 2] + translated_text[-1]

st.text("The Spanish translation of your text is:")
st.text(trimmed_translated_text)

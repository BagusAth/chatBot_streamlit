import google.generativeai as genai
import streamlit as st

api_key = st.secrets["GEMINI_API"]
# Konfigurasi API
genai.configure(api_key=api_key)

# Buat objek model
model = genai.GenerativeModel("gemini-2.0-flash")

# Fungsi untuk mengirim prompt dan dapatkan respon
def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text

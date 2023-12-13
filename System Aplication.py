import subprocess
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Face Recognition For Home Security System',
                          
                          ['Input Database User',
                           'Testing/Implementasi'],
                          icons=['activity','cameras'],
                          default_index=0)

# Input Database User
if (selected == 'Input Database User'):
    
    # page title
    st.title('Input Database User')

    # creating a button for input database
    Hasil = ''

    if st.button('Start to input'):
        # Ganti 'file_lain.py' dengan nama file Python yang ingin kamu jalankan
        file_to_run = 'face1.py'

        # Jalankan file Python lainnya dengan subprocess
        try:
            subprocess.run(['python', file_to_run], check=True)
            Hasil = 'Input Succes'
        except subprocess.CalledProcessError as e:
            print(f"Something wrong: {e}")
            Hasil = 'Input Failed'

    st.success(Hasil)

# Testing/Implementasi
if (selected == 'Testing/Implementasi'):
    
    # page title
    st.title('Testing/Implementasi System')

    # creating a button for input database
    Hasil = ''

    if st.button('Start to input'):
        # Ganti 'file_lain.py' dengan nama file Python yang ingin kamu jalankan
        file_to_run = 'face_recognition.py'

        # Jalankan file Python lainnya dengan subprocess
        try:
            subprocess.run(['python', file_to_run], check=True)
            Hasil = 'System Work'
        except subprocess.CalledProcessError as e:
            print(f"Something wrong: {e}")
            Hasil = 'System Cant Work'

    st.success(Hasil)
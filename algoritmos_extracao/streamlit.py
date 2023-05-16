import streamlit as st
import time
import numpy as np
import json
import subprocess
import os
import io
from tqdm import tqdm



def intro():

    st.write("# Pagaos! 🔆")
    st.sidebar.success("Selecione o script que deseja visualizar.")


def dani_sidebar():
    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    
    if os.path.exists("imoveis.json"):
        os.remove("imoveis.json")

    progress_text = "Por favor, espere até realizarmos sua solicitação!"
    my_bar = st.progress(0, text=progress_text)

    subprocess.run(["python3", "dani.py"], bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(0.1)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1, text=progress_text)

    with open("imoveis.json") as f:
        data = json.load(f)
    st.write(data)


    st.button("Re-run")





def dudu_sidebar():
    st.markdown(f'# {list(page_names_to_funcs.keys())[2]}')
    
    if os.path.exists("imoveis.json"):
        os.remove("imoveis.json")

    progress_text = "Por favor, espere até realizarmos sua solicitação!"
    my_bar = st.progress(0, text=progress_text)

    subprocess.run(["python3", "dudu.py"], bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(0.1)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1, text=progress_text)

    with open("imoveis.json") as f:
        data = json.load(f)
    st.write(data)


    st.button("Re-run")
    




def maria_sidebar():
    st.markdown(f'# {list(page_names_to_funcs.keys())[3]}')
    
    if os.path.exists("imoveis.json"):
        os.remove("imoveis.json")

    progress_text = "Por favor, espere até realizarmos sua solicitação!"
    my_bar = st.progress(0, text=progress_text)

    subprocess.run(["python3", "maria.py"], bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(0.1)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1, text=progress_text)

    with open("imoveis.json") as f:
        data = json.load(f)
    st.write(data)


    st.button("Re-run")


page_names_to_funcs = {
    "Apresentação": intro,
    "dani.py": dani_sidebar,
    "dudu.py": dudu_sidebar,
    "maria.py": maria_sidebar
}

demo_name = st.sidebar.selectbox("Escolha o script", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
import streamlit as st
import time
import numpy as np
import subprocess

def intro():

    st.write("# Pagaos! 🔆")
    st.sidebar.success("Selecione o script que deseja visualizar.")


def dani_sidebar():
    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write("Página da Dani")
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    st.button("Re-run")


def dudu_sidebar():
    st.write("Página do Dudu")

def maria_sidebar():
    st.write("Página da Maria")


page_names_to_funcs = {
    "Apresentação": intro,
    "dani.py": dani_sidebar,
    "dudu.py": dudu_sidebar,
    "maria.py": maria_sidebar
}

demo_name = st.sidebar.selectbox("Escolha o script", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

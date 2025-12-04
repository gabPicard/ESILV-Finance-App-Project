import streamlit as st

st.set_page_config(
    page_title="Menu principal",
    page_icon="📘",
    layout="centered",
)

st.title("Menu principal")
st.markdown("---")

st.header("Choisissez une section")

st.page_link(
    "pages/SingleAsset.py",
    label="Analyse d’un actif (Single Asset)",
    icon="📊"
)

st.page_link(
    "pages/Portfolio.py",
    label="Analyse d’un portefeuille (Portfolio)",
    icon="🧮"
)

st.markdown("---")
st.header("Projet réalisé par")

st.write("**Gabriel PICARD**")  
st.write("**Alex THEAGENE**")  
st.write("**Python, Git, Linux for Finance**  \nIF5")

st.markdown("---")


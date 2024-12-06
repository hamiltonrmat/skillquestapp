import pandas as pd
import streamlit as st

st.title('Informations personelles')

liste_gen = pd.read_excel('https://github.com/hamiltonrmat/skillquestapp/raw/refs/heads/main/liste_gen.xlsx')[['prénom', 'NOM', 'clé', 'mail']]
liste_ml = pd.read_excel('https://github.com/hamiltonrmat/skillquestapp/raw/refs/heads/main/liste_ml.xlsx')[['prénom', 'NOM', 'clé', 'mail']]

cles = pd.DataFrame(liste_gen['clé'])
cles = liste_gen.dropna()

option = st.selectbox(
    "Rentrez une partie de votre nom ou de votre prénom: ",
    [cles.clé[i] for i in range(cles.shape[0])],
    index=None,
    placeholder="NONPrénom: ")

st.write("Votre identifiant: ", option)

agree = st.checkbox("Voir mes informations: ")

if agree:
    st.dataframe(cles[cles['clé'] == option])

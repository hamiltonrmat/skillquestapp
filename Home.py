import streamlit as st

st.title('Maths SkillQuest')

st.write("Tableau de bord pour le suivi de votre situation sur l'ensemble des compétences Mathématiques de SkillQuest")

st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/Informations personnelles.py", label="Informations personnelles", icon="1️⃣")
st.page_link("pages/Détail par compétence.py", label="Détail par compétence", icon="2️⃣")
st.page_link("pages/Situation Générale.py", label="Situation Générale", icon="3️⃣")
st.page_link("https://maths.unilasalle.fr", label="Hub Maths UniLaSalle", icon="🖥️")
st.page_link("https://moodle-beauvais.unilasalle.fr/course/view.php?id=1434", label="Moodle SkillQuest", icon="📚")

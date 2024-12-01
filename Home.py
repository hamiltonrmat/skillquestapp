import streamlit as st

st.title('Maths SkillQuest')

st.write("Tableau de bord pour le suivi de votre situation sur l'ensemble des compétences Mathématique de SkillQuest")

st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/Situation par étudiant.py", label="Situation par étudiant", icon="1️⃣")
st.page_link("pages/Situation générale.py", label="Situation Générale", icon="2️⃣")
st.page_link("https://moodle-beauvais.unilasalle.fr/course/view.php?id=1434", label="Moodle", icon="📖")
st.page_link("https://maths.unilasalle.fr", label="Hub Maths UniLaSalle", icon="📊")

st.image("https://lh3.googleusercontent.com/c5FiAiOTe1P_Af6qK1ORmDPl50O9kLMuFTEntDrgzZuURJvWQ4EvPW9I3SZbjtLOfCIZ9w6hcgdQniEYhaieE8U=w1280")
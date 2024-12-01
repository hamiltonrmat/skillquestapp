import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.title('Maths SkillQuest')

#############
# chemins des fichiers avec les résultats des tentatives
#############

edl = "/Users/hamiltonrmat/Desktop/suivi_maths_skq/edl_maths_skq.xlsx"
file = pd.ExcelFile(edl)
tables = file.sheet_names


################
# Liste Génerale
################
liste_gen = pd.read_excel(edl, sheet_name=tables[-3])
liste_gen = pd.DataFrame(liste_gen['Clé'])
liste_gen = liste_gen.dropna()

################
# exams Maths du Lycée
################

exam1 = pd.read_excel(edl, sheet_name=tables[0])
exam1 = exam1[['Clé', 'Note/20,00']]
exam1 = exam1.groupby(by="Clé").max().reset_index()

exam2 = pd.read_excel(edl, sheet_name=tables[1])
exam2 = exam2[['Clé', 'Note/20,00']]

exam3 = pd.read_excel(edl, sheet_name=tables[2])
exam3 = exam3[['Clé', 'Note/20,00']]

exam4 = pd.read_excel(edl, sheet_name=tables[3])
exam4 = exam4[['Clé', 'Note/20,00']]

exam5 = pd.read_excel(edl, sheet_name=tables[4])
exam5 = exam5[['Clé', 'Note/20,00']]

###
# Ajouter un exam ici
###

##### ajouter un exam en fin de liste
liste_exams_ML = [exam1, exam2, exam3, exam4, exam5]


def get_max(l):
    if len(l) > 0:
        r = max(l)
    else:
        r = np.NaN
    return r



################
# ML
################

for x in range(len(liste_exams_ML)):
    liste_exams_ML[x].columns = ['Clé', 'ml_t'+str(x+1)]

ml = liste_gen.merge(exam1,how='left', on='Clé')
ml = ml.merge(exam2,how='left', on='Clé')
ml = ml.merge(exam3,how='left', on='Clé')
ml = ml.merge(exam4,how='left', on='Clé')
ml = ml.merge(exam5,how='left', on='Clé')

cols_ml = list(ml.columns)
cols_ml.pop(0)

ml['ml_max'] = [get_max([x for x in [ml.iloc[ligne, j] for j in range(1, len(cols_ml)+1)] if x > 0]) for ligne in range(ml.shape[0])]
ml['situation_ml'] = ['pas_de_tentative' if ml['ml_max'].isnull()[i] == True 
                   else 'validé' 
                   if ml['ml_max'][i] >= 10 
                   else 'pas_validé' for i in range(len(ml))]


############@
# Fonctions réelles

exam1 = pd.read_excel(edl, sheet_name=tables[5])
exam1 = exam1[['Clé', 'Note/20,00']]

exam2 = pd.read_excel(edl, sheet_name=tables[6])
exam2 = exam2[['Clé', 'Note/20,00']]

exam3 = pd.read_excel(edl, sheet_name=tables[7])
exam3 = exam3[['Clé', 'Note/20,00']]

###
# Ajouter un exam ici
###

##### ajouter un exam en fin de liste
liste_exams_fr = [exam1, exam2, exam3]

for x in range(len(liste_exams_fr)):
    liste_exams_fr[x].columns = ['Clé', 'fr_t'+str(x+1)]

fr = liste_gen.merge(exam1,how='left', on='Clé')
fr = fr.merge(exam2,how='left', on='Clé')
fr = fr.merge(exam3,how='left', on='Clé')

cols_fr = list(fr.columns)
cols_fr.pop(0)

fr['max_fr'] = [get_max([x for x in [fr.iloc[ligne, j] for j in range(1, len(cols_fr)+1)] if x > 0]) for ligne in range(fr.shape[0])]
fr['situation'] = ['validé' if fr['max_fr'][i] >= 11 else 'pas_validé' for i in range(fr.shape[0])]


###########
## app
###########


type_situation = list(ml.situation_ml.unique())

st.header('Maths du Lycée')

ml_montrer = st.checkbox("Montrer détails", key='ml_c')

if ml_montrer:
    genre = st.radio(
        "Sélectionez une situation: ",
        ["Compétence validé", "Compétence pas validé", "Pas de tentatives"],
        captions=[
            "Validation suite à une ou plusieurs tentatives",
            "Il faut repasser l'examen",
            "Pas concerné ou pas de tentatives",
        ], key="ml")
    if genre == "Compétence validé":
        ml_val = ml[ml['situation_ml'] == 'validé'][['Clé', 'ml_max', 'situation_ml']]
        st.dataframe(ml_val)
        st.write(str(ml_val.shape[0])+' étudiants')
    if genre == "Compétence pas validé":
        ml_pas_val = ml[ml['situation_ml'] == 'pas_validé'][['Clé', 'ml_max', 'situation_ml']]
        st.dataframe(ml_pas_val)
        st.write(str(ml_pas_val.shape[0])+' étudiants')
    if genre == "Pas de tentatives":
        ml_pas_ten = ml[ml['situation_ml'] == 'pas_de_tentative'][['Clé', 'situation_ml']]
        st.dataframe(ml_pas_ten)
        st.write(str(ml_pas_ten.shape[0])+' étudiants')
################

st.header('Fonctions réelles')

fr_montrer = st.checkbox("Montrer détails", key='fr_c')

if fr_montrer:
    genre_fr = st.radio(
        "Sélectionez une situation: ",
        ["Compétence validé", "Compétence pas validé"],
        captions=[
            "Validation suite à une ou plusieurs tentatives",
            "Pas de tentatives ou tentative pas validé"
        ], key='fr')
    if genre_fr == "Compétence validé":
        fr_val = fr[fr['situation'] == 'validé'][['Clé', 'max_fr', 'situation']]
        st.dataframe(fr_val)
        st.write(str(fr_val.shape[0])+' étudiants')
    if genre_fr == "Compétence pas validé":
        fr_pas_val = fr[fr['situation'] == 'pas_validé'][['Clé', 'max_fr', 'situation']]
        st.dataframe(fr_pas_val)
        st.write(str(fr_pas_val.shape[0])+' étudiants')



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

ml['ml_max'] = [max([ml.iloc[x, i] for i in range(1,len(cols_ml)+1)]) for x in range(ml.shape[0])]
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

def get_max(l):
    if len(l) > 0:
        r = max(l)
    else:
        r = np.NaN
    return r

fr['max_fr'] = [get_max([x for x in [fr.iloc[ligne, j] for j in range(1, len(cols_fr)+1)] if x > 0]) for ligne in range(fr.shape[0])]
fr['situation'] = ['validé' if fr['max_fr'][i] >= 11 else 'pas_validé' for i in range(fr.shape[0])]


option = st.selectbox(
    "Rentrez une partie de votre nom ou de votre prénom: ",
    [liste_gen.Clé[i] for i in range(liste_gen.shape[0])],
    index=None,
    placeholder="NONPrénom: ")

st.write("Votre identifiant: ", option)

agree = st.checkbox("Voir ma situation: ")

if agree:
    st.write('Maths du Lycée: ')
    st.dataframe(ml[ml['Clé'] == option])
    st.write('Fonctions réelles: ')
    st.dataframe(fr[fr['Clé'] == option])



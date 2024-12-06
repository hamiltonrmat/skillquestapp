import pandas as pd
import streamlit as st
import plotly.express as px

liste_gen = pd.read_excel('liste_gen.xlsx')[['prénom', 'NOM', 'clé', 'mail']]
liste_ml = pd.read_excel('liste_ml.xlsx')[['prénom', 'NOM', 'clé', 'mail']]
edl = pd.read_excel('edl_maths_skq.xlsx')
file = pd.ExcelFile("edl_maths_skq.xlsx") 
tables_edl = file.sheet_names

############
######## Maths du Lycée
###########

exam1_ml = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[0])
exam1_ml = exam1_ml[['Clé', 'Note/20,00']]
exam1_ml.columns = ['clé', 'note']
exam1_ml = exam1_ml.groupby(['clé']).max().reset_index()

exam2_ml = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[1])
exam2_ml = exam2_ml[['Clé', 'Note/20,00']]
exam2_ml.columns = ['clé', 'note']
exam2_ml = exam2_ml.groupby(['clé']).max().reset_index()

exam3_ml = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[2])
exam3_ml = exam3_ml[['Clé', 'Note/20,00']]
exam3_ml.columns = ['clé', 'note']
exam3_ml = exam3_ml.groupby(['clé']).max().reset_index()

exam4_ml = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[3])
exam4_ml = exam4_ml[['Clé', 'Note/20,00']]
exam4_ml.columns = ['clé', 'note']
exam4_ml = exam4_ml.groupby(['clé']).max().reset_index()

exam5_ml = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[4])
exam5_ml = exam5_ml[['Clé', 'Note/20,00']]
exam5_ml.columns = ['clé', 'note']
exam5_ml = exam5_ml.groupby(['clé']).max().reset_index()

exam6_ml = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[5])
exam6_ml = exam6_ml[['Clé', 'Note/20,00']]
exam6_ml.columns = ['clé', 'note']
exam6_ml = exam6_ml.groupby(['clé']).max().reset_index()

exam7_ml = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[6])
exam7_ml = exam7_ml[['Clé', 'Note/20,00']]
exam7_ml.columns = ['clé', 'note']
exam7_ml = exam7_ml.groupby(['clé']).max().reset_index()

liste_exams_ML = [exam1_ml, exam2_ml, exam3_ml, exam4_ml, exam5_ml, exam6_ml, exam7_ml]

for x in range(len(liste_exams_ML)):
    liste_exams_ML[x].columns = ['clé', 'note_ml_t'+str(x+1)]

ml = liste_ml.merge(exam1_ml, how='left', on='clé')
ml = ml.merge(exam2_ml, how='left', on='clé')
ml = ml.merge(exam3_ml, how='left', on='clé')
ml = ml.merge(exam4_ml, how='left', on='clé')
ml = ml.merge(exam5_ml, how='left', on='clé')
ml = ml.merge(exam6_ml, how='left', on='clé')
ml = ml.merge(exam7_ml, how='left', on='clé')

ml['note_max'] = ml.max(axis='columns', numeric_only=True)

validations_ml = []

for i in range(ml.shape[0]):
    if ml['note_max'].isnull()[i] == True:
        validations_ml.append('pas_de_tentative')
    elif ml['note_max'][i] >= 10:
        validations_ml.append('validé')
    else:
        validations_ml.append('pas_validé')

ml['validation'] = validations_ml


##################
#### Fonctions réelles
##################


exam1_fr = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[7])
exam1_fr = exam1_fr[['Clé', 'Note/20,00']]
exam1_fr.columns = ['clé', 'note']
exam1_fr = exam1_fr.groupby(['clé']).max().reset_index()

exam2_fr = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[8])
exam2_fr = exam2_fr[['Clé', 'Note/20,00']]
exam2_fr.columns = ['clé', 'note']
exam2_fr = exam2_fr.groupby(['clé']).max().reset_index()

exam3_fr = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[9])
exam3_fr = exam3_fr[['Clé', 'Note/20,00']]
exam3_fr.columns = ['clé', 'note']
exam3_fr = exam3_fr.groupby(['clé']).max().reset_index()

exam4_fr = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[10])
exam4_fr = exam4_fr[['Clé', 'Note/20,00']]
exam4_fr.columns = ['clé', 'note']
exam4_fr = exam4_fr.groupby(['clé']).max().reset_index()

liste_exams_FR = [exam1_fr, exam2_fr, exam3_fr, exam4_fr]

for x in range(len(liste_exams_FR)):
    liste_exams_FR[x].columns = ['clé', 'note_fr_t'+str(x+1)]

fr = liste_gen.merge(exam1_fr, how='left', on='clé')
fr = fr.merge(exam2_fr, how='left', on='clé')
fr = fr.merge(exam3_fr, how='left', on='clé')
fr = fr.merge(exam4_fr, how='left', on='clé')

fr['note_max'] = fr.max(axis='columns', numeric_only=True)

validations_fr = []
for i in range(fr.shape[0]):
    if fr['note_max'].isnull()[i] == True:
        validations_fr.append('pas_de_tentative')
    elif fr['note_max'][i] >= 11:
        validations_fr.append('validé')
    else:
        validations_fr.append('pas_validé')
fr['validation'] = validations_fr


##############
### Dérivées
#############

exam1_der = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[11])
exam1_der = exam1_der[['Clé', 'Note/20,00']]
exam1_der.columns = ['clé', 'note']
exam1_der = exam1_der.groupby(['clé']).max().reset_index()

exam2_der = pd.read_excel('edl_maths_skq.xlsx', sheet_name=tables_edl[12])
exam2_der = exam2_der[['Clé', 'Note/20,00']]
exam2_der.columns = ['clé', 'note']
exam2_der = exam2_der.groupby(['clé']).max().reset_index()

liste_exams_der = [exam1_der, exam2_der]

for x in range(len(liste_exams_der)):
    liste_exams_der[x].columns = ['clé', 'note_der_t'+str(x+1)]

der = liste_gen.merge(exam1_der, how='left', on='clé')
der = der.merge(exam2_der, how='left', on='clé')

der['note_max'] = der.max(axis='columns', numeric_only=True)

validations_der = []
for i in range(der.shape[0]):
    if der['note_max'].isnull()[i] == True:
        validations_der.append('pas_de_tentative')
    elif der['note_max'][i] >= 11:
        validations_der.append('validé')
    else:
        validations_der.append('pas_validé')
der['validation'] = validations_der



st.title("Situation générale")
st.caption("Vue d'ensemble sur toutes les compétences")



competences = ["Maths du Lycée", "Fonctions Réelles", "Dérivées"]
df_competences = [ml, fr, der]

ml_valid = pd.DataFrame(ml.validation.value_counts()).reset_index()
ml_valid.columns = ['validation', "Maths du Lycée"]

fr_valid = pd.DataFrame(fr.validation.value_counts()).reset_index()
fr_valid.columns = ['validation', "Fonctions Réelles"]

der_valid = pd.DataFrame(der.validation.value_counts()).reset_index()
der_valid.columns = ['validation', "Dérivées"]

situation_gen = ml_valid.merge(fr_valid, how='left', on='validation')
situation_gen = situation_gen.merge(der_valid, how='left', on='validation')
situation_gen = situation_gen.set_index('validation')
fig = px.bar(situation_gen, barmode='group', height=430)
st.plotly_chart(fig)

st.dataframe(situation_gen)
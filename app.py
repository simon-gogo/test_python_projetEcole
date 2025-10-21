import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Analyse énergétique - Oise", layout="wide")

# ==============================================================
# 1) PROBLÉMATIQUE RÉELLE (LIEN AVEC LA SPÉCIALITÉ GRT)
# ==============================================================

st.markdown("<h1 style='text-align: center;'>I. Problématique réelle (Lien avec la spécialité GRT)</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>GODART Simon, BAYVET Guillaume (promo 086)</h3>", unsafe_allow_html=True)

st.markdown("""#### Comment relier les consommations énergétiques de certains secteurs des communes de l’Oise pour pouvoir estimer celles d’autres secteurs dans ces mêmes territoires ?""")

# ==============================================================
# 2) FORMULATION DE LA QUESTION PRATIQUE — APPROCHE DATA SCIENCE
# ==============================================================

st.markdown("<h1 style='text-align: center;'>II. Formulation de la question pratique (Approche *Data Sciences*)</h1>", unsafe_allow_html=True)

st.markdown("""### **Techniques mobilisées :**
- *Traitements de données* 
- *Data mining*  
- *Machine learning* """)  

st.markdown("""### **Question pratique :** """)  
st.markdown("""*Comment construire une prédiction qui soit basée sur les consommations énergétiques de plusieurs secteurs répartis sur différentes communes de l’Oise, afin d’estimer la consommation énergétique d’autres secteurs qui n’ont pas été mesurées ?*""")

# ==============================================================
# TRAITEMENTS DE DONNÉES
# ==============================================================

st.markdown("""### Traitements de données """)
st.markdown("""*Réaliser un pré-traitement des données énergétiques en :  
- **Les nettoyant** : compléter les données énergétiques issues du fichier CSV, 
  qui sont manquantes, bruitées, aberrantes ou incohérentes.  
- **Les intégrant** : combiner les différentes colonnes et fichiers liés à la question pratique.  
- **Les transformant** : ajuster les valeurs pour les insérer dans un intervalle précis.  
- **Les réduisant** : rendre les données moins volumineuses et plus accessibles.  
- **Les discrétisant** : créer différentes étiquettes de consommation (ou catégories) 
  pour remplacer les intervalles continus par des classes. """)

# ==============================================================
# ÉTAPES DE TRAITEMENT
# ==============================================================

st.markdown("""### Étapes de traitement à réaliser pour y répondre"
1. Nettoyage et préparation des données *(pandas, numpy)*  
2. Analyse statistique descriptive *(moyenne, médiane, écart-type)*  
3. Visualisation temporelle *(matplotlib, seaborn)*  
4. Calcul d’indicateurs de performance énergétique""")

st.info("NOTE : Ces étapes serviront de base pour développer le modèle prédictif des consommations énergétiques.")

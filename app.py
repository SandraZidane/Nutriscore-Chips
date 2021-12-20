import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd


# Les images utilisées :
page_icon = Image.open('assets/icon.png')
image_chips = Image.open('assets/chips.png')
image_artefact = Image.open('assets/Artefact.png')
image_nutri_a = Image.open('assets/nutriscore_a.png')
image_nutri_b = Image.open('assets/nutriscore_b.png')
image_nutri_c = Image.open('assets/nutriscore_c.png')
image_nutri_d = Image.open('assets/nutriscore_d.png')
image_nutri_e = Image.open('assets/nutriscore_e.png')



# Nom de la page :
st.set_page_config(
        page_title = "Nutriscore chips",
        page_icon = image_artefact, # icone de nom de page
        layout = "wide" # Ou "centered" si on veut mettre une marge
)


# Titre :
st.markdown("# Quel est le nutriscore de vos chips préférés ?")


#st.image(page_icon)


# DataFrame :
df = pd.read_csv("output_chips.csv")
#df


# Dans la marge :
add_selectbox = st.sidebar.markdown(
    "# ARTEFACT School of Data"
)

add_selectbox = st.sidebar.image(image_artefact)

add_selectbox = st.sidebar.markdown(
    "Cette application fournit le nutriscore de tous les paquets de chips sur le marché :"
)

#st.sidebar.info("dommage")
#st.sucess, st.warning, st.error and st.exception

add_selectbox = st.sidebar.markdown(
    "- Elle indique le nutriscore d'un paquet de chips s'il existe déjà"
)

add_selectbox = st.sidebar.markdown(
    "- Elle estime le nutriscore d'un paquet s'il n'existe pas"
)


# Dans le cadre principal :
barcode_user = st.selectbox(
     'Indiquez le code barre du paquet de chips qui vous fait envie :',
     (df["barcode"]))


df_user = df[df["barcode"] == barcode_user]
#df_user
product_user = list(df_user["product_name"])[0]
url_user = list(df_user["url_openfoodfact"])[0]
# Features :
brand_user = list(df_user["brands"])[0]
pnns_user = list(df_user["pnns_groups_1"])[0]
nb_addi_user = str(list(df_user["additives_n"])[0])
fat_user = str(list(df_user["fat_100g"])[0])
protein_user = str(list(df_user["proteins_100g"])[0])
salt_user = str(list(df_user["salt_100g"])[0])
sodium_user = str(list(df_user["sodium_100g"])[0])
sugars_user = str(list(df_user["sugars_100g"])[0])
energy_user = str(list(df_user["energy_100g"])[0])
carbo_user = str(list(df_user["carbohydrates_100g"])[0])
palm_oil_user = str(list(df_user["ingredients_from_palm_oil_n"])[0])
maybe_palm_oil_user = str(list(df_user["ingredients_that_may_be_from_palm_oil_n"])[0])
# Target :
nutriscore_user = str(list(df_user["nutriscore_grade"])[0])
nutriscore_description = list(df_user["nutri_descr"])[0]
# Prédictions :
pred_log_reg_user = str(list(df_user["pred_log_reg"])[0])
pred_tree_user = str(list(df_user["pred_tree"])[0])
pred_rand_for_user = str(list(df_user["pred_rand_for"])[0])
pred_ada_boost_user = str(list(df_user["pred_ada_boost"])[0])
pred_grad_boost_user = str(list(df_user["pred_grad_boost"])[0])
pred_xg_boost_user = str(list(df_user["pred_xg_boost"])[0])
pred_log_reg_descr_user = str(list(df_user["pred_log_reg_descr"])[0])
pred_tree_descr_user = str(list(df_user["pred_tree_descr"])[0])
pred_rand_for_descr_user = str(list(df_user["pred_rand_for_descr"])[0])
pred_ada_boost_descr_user = str(list(df_user["pred_ada_boost_descr"])[0])
pred_grad_boost_descr_user = str(list(df_user["pred_grad_boost_descr"])[0])
pred_xg_boost_descr_user = str(list(df_user["pred_xg_boost_descr"])[0])


st.write('Le code barre ', barcode_user, 'correspond au produit ', product_user, 'de', brand_user,".")


col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Caractéristiques du produit :")
    st.write("Catégorie : ", pnns_user)
    st.write("Nombre d'additifs : ", nb_addi_user)
    st.write("Nombre d'ingrédients issus de l'huile de palme : ", palm_oil_user)
    st.write("Nombre d'ingrédients pouvant être issus de l'huile de palme : ", maybe_palm_oil_user)

    st.markdown("#### Informations nutritionnelles pour 100 g:")
    st.write("Energie : ", energy_user, " kj")
    st.write("Matières grasses : ", fat_user, "g")
    st.write("Protéines : ", protein_user, "g")
    st.write("Sel : ", salt_user, "g")
    st.write("Sodium : ", sodium_user, "g")
    st.write("Sucres : ", sugars_user, "g")



with col2:
    if nutriscore_user in ("A", "B", "C", "D", "E"):
        st.markdown("#### Nutri-score du produit :")
        st.write("Son Nutri-Score est ", nutriscore_user, ".")
        st.write("Qualité nutritionnelle : ", nutriscore_description)
        if nutriscore_user == "A":
            st.image(image_nutri_a)
        elif nutriscore_user == "B":
            st.image(image_nutri_b)
        elif nutriscore_user == "C":
            st.image(image_nutri_c)
        elif nutriscore_user == "D":
            st.image(image_nutri_d)
        elif nutriscore_user == "E":
            st.image(image_nutri_e)
        st.info("Cette information est fournie par le fabricant.")
    else:
        st.markdown("#### Nutri-score estimé du produit :")
        algo_user = st.selectbox(
             'Choisissez un algorithme de classification:',
             ("Régression logistique",  "Arbre de décision",
              "Random Forest",          "Adaptative Boosting",
              "Gradient Boosting",      "XG Boost"))


        # Regression logistique
        if algo_user == "Régression logistique":
            st.write("Le Nutri-Score estimé du produit est ", pred_log_reg_user, ".")
            st.write("Qualité nutritionnelle : ", pred_log_reg_descr_user)
            if pred_log_reg_user == "A":
                st.image(image_nutri_a)
            elif pred_log_reg_user == "B":
                st.image(image_nutri_b)
            elif pred_log_reg_user == "C":
                st.image(image_nutri_c)
            elif pred_log_reg_user == "D":
                st.image(image_nutri_d)
            elif pred_log_reg_user == "E":
                st.image(image_nutri_e)
        # Arbre de décision
        elif algo_user == "Arbre de décision":
            st.write("Le Nutri-Score estimé du produit est ", pred_tree_user, ".")
            st.write("Qualité nutritionnelle : ", pred_tree_descr_user)
            if pred_tree_user == "A":
                st.image(image_nutri_a)
            elif pred_tree_user == "B":
                st.image(image_nutri_b)
            elif pred_tree_user == "C":
                st.image(image_nutri_c)
            elif pred_tree_user == "D":
                st.image(image_nutri_d)
            elif pred_tree_user == "E":
                st.image(image_nutri_e)
        # Random Forest
        elif algo_user == "Random Forest":
            st.write("Le Nutri-Score estimé du produit est ", pred_rand_for_user, ".")
            st.write("Qualité nutritionnelle : ", pred_rand_for_descr_user)
            if pred_rand_for_user == "A":
                st.image(image_nutri_a)
            elif pred_rand_for_user == "B":
                st.image(image_nutri_b)
            elif pred_rand_for_user == "C":
                st.image(image_nutri_c)
            elif pred_rand_for_user == "D":
                st.image(image_nutri_d)
            elif pred_rand_for_user == "E":
                st.image(image_nutri_e)
        # Ada Boost
        elif algo_user == "Adaptative Boosting":
            st.write("Le Nutri-Score estimé du produit est ", pred_ada_boost_user, ".")
            st.write("Qualité nutritionnelle : ", pred_ada_boost_descr_user)
            if pred_ada_boost_user == "A":
                st.image(image_nutri_a)
            elif pred_ada_boost_user == "B":
                st.image(image_nutri_b)
            elif pred_ada_boost_user == "C":
                st.image(image_nutri_c)
            elif pred_ada_boost_user == "D":
                st.image(image_nutri_d)
            elif pred_ada_boost_user == "E":
                st.image(image_nutri_e)
        # Gradient Boost
        elif algo_user == "Gradient Boosting":
            st.write("Le Nutri-Score estimé du produit est ", pred_grad_boost_user, ".")
            st.write("Qualité nutritionnelle : ", pred_grad_boost_descr_user)
            if pred_grad_boost_user == "A":
                st.image(image_nutri_a)
            elif pred_grad_boost_user == "B":
                st.image(image_nutri_b)
            elif pred_grad_boost_user == "C":
                st.image(image_nutri_c)
            elif pred_grad_boost_user == "D":
                st.image(image_nutri_d)
            elif pred_grad_boost_user == "E":
                st.image(image_nutri_e)
        # XG Boost
        elif algo_user == "XG Boost":
            st.write("Le Nutri-Score estimé du produit est ", pred_xg_boost_user, ".")
            st.write("Qualité nutritionnelle : ", pred_xg_boost_descr_user)
            if pred_xg_boost_user == "A":
                st.image(image_nutri_a)
            elif pred_xg_boost_user == "B":
                st.image(image_nutri_b)
            elif pred_xg_boost_user == "C":
                st.image(image_nutri_c)
            elif pred_xg_boost_user == "D":
                st.image(image_nutri_d)
            elif pred_xg_boost_user == "E":
                st.image(image_nutri_e)
        # Autres
        else:
            st.write("Une erreur s'est produite. Merci de sélectionner un autre produit.")

        st.info("Cette information n'est pas fournie par le fabricant. Il s'agit d'une estimation.")




st.text(url_user)

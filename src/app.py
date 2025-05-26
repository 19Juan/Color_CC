from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import streamlit as st
import json
import pickle
import numpy as np

with open('/workspaces/Color_CC/models/Lineal_Regressor_Color_Club.sav', 'rb') as file:
    model = pickle.load(file)
    
#with open('/workspaces/Color_CC/models/Random_Forest_Color_Club.sav', 'rb') as file:
#    model = pickle.load(file)



#with open('../data/processed/dic_cl.json','r', encoding='utf-8') as archivo:
#    dic_cl = json.load(archivo)
#with open('../data/processed/dic_el.json','r', encoding='utf-8') as archivo:
#    dic_el = json.load(archivo)
#with open('../data/processed/dic_et.json','r', encoding='utf-8') as archivo:
#    dic_et = json.load(archivo)
#with open('../data/processed/dic_er.json','r', encoding='utf-8') as archivo:
#    dic_er = json.load(archivo)
#with open('../data/processed/dic_cs.json','r', encoding='utf-8') as archivo:
#    dic_cs = json.load(archivo)
# Configuración de la página y tema personalizados

st.set_page_config(
    page_title="Predicción del color por cocimiento de la Club Colombia",
    page_icon="🍺",
    layout="wide"
)


st.title("Predicción del color por cocimiento de la Club Colombia 🍺")
st.markdown("""
    Esta aplicación predice el color del cocimiento de la cerveza Club Colombia.
    Ajusta los parámetros a continuación para ver la predicción del color en EBC.
""")

#val1 = st.number_input("¿Cuántos kilogramos de malta tiene el cocimiento?", 
#min_value=17300, 
#    max_value=18600, 
#    value=0,  # valor inicial
#    step=1)
val1 = st.slider("¿Cuántos bultos de malta caramelo vas a dosificar?", min_value = 6, max_value = 26, step = 1)
val2 = st.slider("¿Cuál es el poder colorante de la malta caramelo?", min_value = 120, max_value = 160, step = 1)
val3 = st.slider("Cuál es el color ponderado del silo?", min_value = 3.5, max_value = 4.7, step = 0.1)


#val6 = st.selectbox(
#    "Pais de Residencia del Empleado",
#    (dic_er.keys()),
#    index=None,
#    placeholder="Selecciona el pais...",
#)

#val7 = st.selectbox(
#    "Pais de Origen de la Compañia",
#    (dic_cl.keys()),
#    index=None,
#    placeholder="Selecciona el pais...",
#)


if st.button("Predecir"):
    # Create input array and reshape for prediction
    X_pred = np.array([val1, val2, val3]).reshape(1, -1)
    prediction = model.predict(X_pred)[0]
    st.write(f"El color del cocimiento será: {prediction:.2f} EBC")
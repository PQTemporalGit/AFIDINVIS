from click import option
from auxiliar import *
import streamlit as st 
import pandas as pd

def app():
    st.title("Comparador del desarrollo del covid por países")

    st.write("El tiempo pasa y los datos siguen aumentando. Esta herramienta te permitirá realizar "+\
    "comparaciones de hasta 5 paises simultaneamente. Solamente tienes que elegir cúantos "+\
    "paises quieres comparar y seleccionarlos en el menú de desplegables. Empecemos!")
    
    consejo = "Consejo: No necesitas ir rodando hasta encontrar el pais que buscas, puedes escribir "+\
        "la inicial de cada país y seleccionarlo entre las opciones recomendadas"
    st.write(consejo)


    num_paises = st.slider('Seleccione el número de paises que desea comparar:', min_value=1, max_value=5,
                        value=2) 

    options = []
    value = [29,74,5,10,15]
    for n_pais in range(num_paises):
        options.append(st.selectbox(
        'Seleccione país número ' + str(n_pais+1),
        nombres_paises(), index=value[n_pais]))

    fig = go.Figure(data = traza_paises(options))
    st.plotly_chart(fig)
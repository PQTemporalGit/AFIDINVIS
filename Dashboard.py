import streamlit as st 

import Comparador
import Mapa
import Intro
import Evolucion
import Metricas

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


st.sidebar.title('Herramientas para el análisis del Covid-19')
st.sidebar.header('Opciones:')

PAGES = {
    "Introducción": Intro,
    "Graficos Covid-19": Comparador,
    "Mapamundi Covid-19": Mapa,
    "Evolución Covid-19": Evolucion,
    "Métricas Covid-19 mediante API": Metricas
}

selection = st.sidebar.radio("Seleccione una pestaña:", list(PAGES.keys()))


page = PAGES[selection]
page.app()
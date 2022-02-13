import streamlit as st
import plotly.express as px 
from auxiliar import *

def app():
    st.title("Esto es un comparador de casos según dia y país")
    
    intro = "Esta herramienta muestra el mapamundi separado por colores según el numero de casos. "+\
        "Basta seleccionar si queremos la segregación por casos nuevos o casos totales y posteriormente, "+\
        "seleccionar el dia, mes y año del que queremos hacer la consulta."
    st.write(intro)
    
    preg0 = "Seleccione si desea realizar la comparacion por casos nuevos o casos totales:"
    st.write(preg0)
    
    casos =st.selectbox(
        'Seleccione la modalidad',
        ["Casos nuevos", "Casos totales"], index=1)
    
    moda = {
        "Casos nuevos": "new_cases",
        "Casos totales": "total_cases"
    }
    
    preg1 = "A continuación, seleccione el año, el mes y el día deseado:"
    st.write(preg1)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        dia = st.selectbox(
        'Seleccione el dia',
        [i+1 for i in range(31)], index=20)
        
    with col2:
        mes = st.selectbox(
        'Seleccione el mes',
        [i+1 for i in range(12)], index=2)
        
    with col3:
        anho = st.selectbox(
        'Seleccione el año',
        [2020,2021,2022], index=0)

    fig = mapamundi(dia, mes, anho, moda[casos])
    st.plotly_chart(fig)

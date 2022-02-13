import streamlit as st 
from funcionesAPI import *
import pandas as pd

def app():
    
    st.title("Estas son métricas obtenidas a tiempo real mediante una API")
    
    st.write("Los datos se presentarán de la siguiente manera, la primera fila contendrá "+\
        "informacion de la region. El simbolo muestra el aumento del porcentaje con respecto al" +
        "país. En la siguiente fila se muestran los datos del país seleccionado, con los porcentajes "+\
        "respecto al total.")
    
    st.write("Seleccione las siguientes informaciones.")
    paises = paises_disponibles()
    id_espanha = paises.index("Spain")
    
    pais = st.selectbox(
        'Seleccione el pais',
        paises, index=id_espanha)
    
    regiones = obten_regiones(pais)
    region = st.selectbox(
        'Seleccione la región',
        regiones, index=0)
    
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
    datos_reg = datos_region(pais, region, dia, mes, anho)
    serie = pd.Series(np.array(list(datos_reg.values())), index=datos_reg.keys())
    datos_reg = pd.DataFrame(serie).transpose()
    
    datos_contry = datos_pais(pais, dia, mes, anho)
    fallecimientos, nuevos_fallecimientos = datos_contry["today_deaths"], datos_contry["today_new_deaths"]
    porcent_fallecimientos = str(100*int(datos_reg["Fallecimientos hoy"])/fallecimientos)[:4]+"%"
    porcent_casos = str(100*int(datos_reg["Casos abiertos hoy"])/datos_contry["today_new_open_cases"])[:4]+"%"
    confirmados_porcent = str(100*int(datos_reg["Nuevos casos confirmados"])/datos_contry["today_new_confirmed"])[:4]+"%"

    col1.metric(label = "Casos confirmados hoy", value = datos_reg["Nuevos casos confirmados"], delta = confirmados_porcent)
    col2.metric(label = "Fallecimientos hoy", value = datos_reg["Fallecimientos hoy"], delta = porcent_fallecimientos)
    col3.metric(label = "Casos abiertos hoy", value = datos_reg["Casos abiertos hoy"], delta = porcent_casos)
    
    aumento_confirmados = str(100*int(datos_contry["today_new_confirmed"])/datos_contry["today_confirmed"])[:4]+"%"
    col1.metric(label = "Casos confirmados hoy", value = datos_contry["today_confirmed"], delta = aumento_confirmados)
    
    aumento_abiertos = str(100*int(datos_contry["today_new_open_cases"])/datos_contry["today_open_cases"])[:4]+"%"
    col2.metric(label = "Fallecimientos Hoy", value = fallecimientos, delta = nuevos_fallecimientos)
    col3.metric(label = "Casos abiertos hoy", value = datos_contry["today_open_cases"], delta = aumento_abiertos)
    
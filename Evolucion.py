import streamlit as st 
from auxiliar import *
from time import sleep

def app():
    st.title("Evolución Covid-19")
    
    desc1 = "Con estos graficos puedes deslizar la barra por las distintas fechas e ir viendo los principales " +\
        "puntos de contagio a lo largo del tiempo. Además, puedes configurar si quieres verlo según contagios totales "+\
        "o si prefieres visualizarlo por contagios diarios. Elige lo que prefieras!"
    st.write(desc1)
    
    casos =st.selectbox(
        'Seleccione la modalidad',
        ["Casos nuevos", "Casos totales"], index=0)
    
    moda = {
        "Casos nuevos": "new_cases",
        "Casos totales": "total_cases"
    }
    #pressionado = st.button('Inicia el proceso')
    
    total_dates = dias_totales()
    value = total_dates[0]
    
    # if pressionado:
    #     for date in total_dates:
    #         sleep(1)
    #         value = date
    #         st.empty()

    date = st.select_slider(
        'Selecciona la fecha donde inciar',
        options=total_dates,
        value=value)
    
    st.plotly_chart(bouble_map(date, moda[casos]))

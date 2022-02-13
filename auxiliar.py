from typing import List
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

covid = pd.read_csv('covid_incomplete.csv')
covid['new_cases'] = covid['new_cases'].fillna(0)
covid['total_cases'] = covid['total_cases'].fillna(0)

def columna_i(i: int):
    col_names = covid.columns
    return covid[col_names[i]]

def nombres_paises():
    """Devuelve los paises ordenados en forma de tupla"""
    unique_countries = list(set(covid["location"]))
    unique_countries.sort()
    return tuple(unique_countries)

def datos_paises(paises: List):
    """
    Retorna los datos de los paises del dataframe seleccionados.
    
    Params:
    paises (List[str]) : Lista de los paises que queremos selecionar en formato
    string.
    """
    return covid[covid["location"].isin(paises)]

def trace_seleccionado(nombre_pais):
    """Obtiene la traza necesaria para el dibujo del pais con nombre en el origen"""
    return go.Scatter(
        x=datos_paises([nombre_pais])['date'], 
        y=datos_paises([nombre_pais])['new_cases'],
        mode = "lines",
        name = nombre_pais
    )

def traza_paises(paises):
    trazas = [trace_seleccionado(pais) for pais in paises]
    return trazas

def digit2text(digit):
    text = str(digit)
    return text if len(text)==2 else "0"+text

def mapamundi(dia, mes, anho, modalidad):
    dia = str(anho) +"-"+ digit2text(mes) +"-"+ digit2text(dia)
    df = covid[covid["date"]== dia]
    try:
        maxim = max(df[modalidad])/3
    except:
        maxim = 0
    fig = px.choropleth(df, locations="iso_code",
                        color = modalidad,
                        hover_name = "location", 
                        range_color=(0, maxim),
                        color_continuous_scale = px.colors.sequential.Reds)
    return fig

def bouble_map(date, modalidad):
    dia = date
    df = covid[covid["date"]== dia]
    df = df[df[modalidad]>20]
    try:
        try:
            maxim = max(df[modalidad])/3
            arr = np.array(df[modalidad])
            values = arr/max(arr)/3+0.01
        except:
            maxim = 0
            values = [0]*len(df["location"])
        fig = px.scatter_geo(df, locations="iso_code", color=df[modalidad],
                        hover_name="location", size=values,
                        range_color=(0,maxim/4),
                        animation_frame="date",
                        color_continuous_scale = px.colors.sequential.Blues,
                        projection="natural earth")
        return fig
    except:
        pass
    return None

def dias_totales():
    opciones = []
    anhos = [2020,2021]
    dias_en_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
    meses = {
        0: "Enero",
        1: "Febrero", 
        2: "Marzo",
        3: "Abril",
        4:"Mayo",
        5: "Junio",
        6: "Julio",
        7:"Agosto",
        8:"Septiembre",
        9:"Octubre",
        10:"Noviembre",
        11:"Diciembre"
    }
    for anho in anhos:
        for mes in meses.keys():
            for dia in range(dias_en_mes[mes]):
                if(anho == 2020 and mes == 0 and dia<22):
                    continue
                date = str(anho) +"-"+ digit2text(mes+1) +"-"+ digit2text(dia+1)
                opciones.append(date)
    return opciones
            
import requests
import pandas as pd
import numpy as np

def digit2text(digit):
    text = str(digit)
    return text if len(text)==2 else "0"+text

    

def obten_regiones(nombre_pais):
    resp = requests.get("https://api.covid19tracking.narrativa.com/api/countries/"+nombre_pais+"/regions")
    diccionario = dict(resp.json())
    di = diccionario["countries"][0]
    regiones = []
    for i in di[nombre_pais]:
        regiones.append(i["name"])
    regiones.sort()
    return regiones

def obten_n_regiones(nombre_pais):
    len(obten_regiones(nombre_pais))
    
def paises_disponibles():
    resp = requests.get("https://api.covid19tracking.narrativa.com/api/countries")
    diccionario = dict(resp.json())
    diccionario = diccionario["countries"]
    paises = [pais_info["name"] for pais_info in diccionario]
    paises.sort()
    return paises

def datos_region(pais,region, dia, mes, anho):
    fecha = str(anho) +"-"+ digit2text(mes) +"-"+ digit2text(dia)
    resp = requests.get("https://api.covid19tracking.narrativa.com/api/"+fecha+"/country/"+pais+"/region/"+region)
    diccionario = dict(resp.json())
    datos = diccionario['dates'][list(diccionario['dates'].keys())[0]]["countries"][pais]["regions"][0]
    recopilacion1 = {
        "Nuevos casos confirmados": datos["today_new_confirmed"],
        "Fallecimientos hoy": datos["today_new_deaths"],
        "Casos abiertos hoy": datos["today_open_cases"]
    }
    return recopilacion1

def datos_pais(pais, dia, mes, anho):
    fecha = str(anho) +"-"+ digit2text(mes) +"-"+ digit2text(dia)
    resp = requests.get("https://api.covid19tracking.narrativa.com/api/"+fecha+"/country/"+pais)
    diccionario = dict(resp.json())
    dates = diccionario["dates"]
    datos = dates[list(dates.keys())[0]]['countries'][pais]
    recopilacion = {
        "today_new_confirmed": datos["today_new_confirmed"],
        "today_confirmed": datos["today_confirmed"],
        "today_new_confirmed": datos["today_new_confirmed"],
        "today_deaths": datos["today_deaths"],
        "today_new_deaths": datos["today_new_deaths"],
        "today_new_open_cases": datos["today_new_open_cases"],
        "today_open_cases": datos["today_open_cases"],
    }
    return recopilacion


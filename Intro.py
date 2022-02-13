from PIL import Image
import streamlit as st 

def app():
    intro = "Introducción"
    st.title(intro)
    
    descripcion = "Durante estos años de pandemia, nos hemos visto expuestos a análisis de " +\
    "muchos expertos. Sin embargo, es dificil encontrar una herramienta rápida que nos permita analizar "+\
    "por nosotros mismos. Aquí se reunen un conjunto sencillo de herramientas que nos permiten visualizar "+\
    "los casos de covid a lo largo del tiempo." 
    st.write(descripcion)
    
    img_covid = Image.open("intro_covid.jpg").resize((700,300))
    st.image(img_covid)
    


    descripcion2 = "Para empezar. selecciona cualquier herramienta del menú de la izquierda y prueba "+\
    "a ir cambiando las opciones tú mismo"
    st.write(descripcion2)
import pandas as pd
import plotly.express as px # type: ignore
import streamlit as st

st.header("estadistica de autos")    
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('contruir grafico de disperción')

if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de disperción para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    # crear una casilla de verificación

build_boxplot = st.checkbox('Construir un bloxplot')

if build_boxplot: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna color de la pintura')

    fig = px.box(car_data, x = "condition", y = "price", color = 'paint_color')
    
    st.plotly_chart(fig, use_container_width=True)

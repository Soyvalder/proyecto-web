import pandas as pd 
import plotly.express as px 
import streamlit as st 
  
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.title('Análisis de Datos de Vehículos')

hist_botton = st.button('construir Histograma')
#scatter_plot_button = st.button('construir grafico de dispersion')

if hist_botton:
    st.write('creacion de un histograma para el conjunto de datos')
    
    fig = px.histogram(car_data, x='odometer', nbins = 20)
    st.plotly_chart(fig, use_container_width = True)
    

# Casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un diagrama de dispersión')

if build_histogram:  # Si la casilla de verificación para el histograma está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig_histogram = px.histogram(car_data, x='odometer')  # Usar la columna 'odometer'
    st.plotly_chart(fig_histogram)

if build_scatter:  # Si la casilla de verificación para el diagrama de dispersión está seleccionada
    st.write('Construir un diagrama de dispersión para las columnas precio y año de modelo')
    fig_scatter = px.scatter(car_data, x='model_year', y='price')  # Usar 'model_year' y 'price'
    st.plotly_chart(fig_scatter)
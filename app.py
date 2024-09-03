import pandas as pd 
import plotly.express as px 
import streamlit as st 
  
car_data = pd.read_csv('vehicles_us.csv')

hist_botton = st.button('construir Histograma')
#scatter_plot_button = st.button('construir grafico de dispersion')

if hist_botton:
    st.write('creacion de un histograma para el conjunto de datos')
    
    fig = px.histogram(car_data, x='odometer', nbins = 20)
    st.plotly_chart(fig, use_container_width = True)
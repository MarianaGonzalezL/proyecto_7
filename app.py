import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv('vehicles_us.csv')

# Crear encabezado
st.header('Análisis de Datos de Vehículos')

# Botón para construir histograma
if st.button('Construir Histograma'):
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(df, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir gráfico de dispersión
if st.button('Construir Gráfico de Dispersión'):
    st.write('Creación de un gráfico de dispersión para la relación entre el precio y el odómetro')
    fig_scatter = px.scatter(df, x='odometer', y='price', title='Precio vs Kilometraje')
    st.plotly_chart(fig_scatter, use_container_width=True)



import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Creación de un histograma para la columna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión: relación entre odómetro y precio')
    fig2 = px.scatter(car_data, x="odometer", y="price", title="Kilometraje vs Precio")
    st.plotly_chart(fig2, use_container_width=True)
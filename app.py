
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard ChatGPT y Programación",
    layout="wide"
)

st.title("📚 Dashboard Bibliométrico")

st.subheader(
    "¿Cómo influye el uso de ChatGPT en el aprendizaje de programación de estudiantes universitarios?"
)

archivo = st.file_uploader(
    "Cargar archivo CSV de Scopus",
    type=["csv"]
)

if archivo is not None:

    df = pd.read_csv(archivo)

    col1, col2, col3 = st.columns(3)

    col1.metric("Artículos", df.shape[0])

    col2.metric("Columnas", df.shape[1])

    col3.metric("Año más reciente", int(df["Year"].max()))

    st.subheader("Vista previa del dataset")

    st.dataframe(df)

import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Dashboard ChatGPT y Programación",
    layout="wide"
)

# Título
st.title("📚 Dashboard Bibliométrico")

st.subheader(
    "¿Cómo influye el uso de ChatGPT en el aprendizaje de programación de estudiantes universitarios?"
)

# Descripción
st.markdown("""
Este dashboard presenta un análisis bibliométrico de artículos científicos obtenidos desde Scopus relacionados con el uso de ChatGPT en el aprendizaje de programación.
""")

# Opción para cargar otro archivo CSV
archivo = st.file_uploader(
    "Cargar otro archivo CSV de Scopus (opcional)",
    type=["csv"]
)

# Si el usuario sube un archivo, se usa ese.
# Si no, se usa el dataset incluido en el repositorio.
if archivo is not None:
    df = pd.read_csv(archivo)
else:
    df = pd.read_csv("dataset_grupo1.csv")

# Métricas principales
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Artículos", df.shape[0])

with col2:
    st.metric("Columnas", df.shape[1])

with col3:
    st.metric("Año más reciente", int(df["Year"].max()))

# Vista previa
st.subheader("📄 Vista previa del dataset")

st.dataframe(df)

# Información del proyecto
st.markdown("---")
st.markdown("""
**Grupo 1**

**Pregunta de investigación:**  
¿Cómo influye el uso de ChatGPT en el aprendizaje de programación de estudiantes universitarios?
""")

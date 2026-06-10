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

# Filtros
st.sidebar.header("🔍 Filtros")

años = sorted(df["Year"].dropna().unique())

años_seleccionados = st.sidebar.multiselect(
    "Selecciona los años",
    años,
    default=años
)

df_filtrado = df[df["Year"].isin(años_seleccionados)]

# Métricas principales
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Artículos", df_filtrado.shape[0])
    
with col2:
    st.metric("Columnas", df.shape[1])

with col3:
    st.metric("Año más reciente", int(df["Year"].max()))

# Vista previa
st.subheader("📄 Vista previa del dataset")

st.dataframe(df_filtrado)

# Producción científica por año
st.subheader("📈 Producción científica por año")

articulos_anio = df_filtrado["Year"].value_counts().sort_index()

st.bar_chart(articulos_anio)

# Artículos más citados
st.subheader("🏆 Top 10 artículos más citados")

top_citados = df_filtrado[["Title", "Cited by"]].sort_values(
    by="Cited by",
    ascending=False
).head(10)

st.dataframe(top_citados)

# Tipos de documento
st.subheader("📄 Tipos de documento")

tipos = df_filtrado["Document Type"].value_counts()

st.bar_chart(tipos)

# Open Access
st.subheader("🔓 Open Access")

open_access = df_filtrado["Open Access"].value_counts()

st.bar_chart(open_access)

# Fuentes con más publicaciones
st.subheader("👨‍🔬 Autores más productivos")

autores = (
    df_filtrado["Authors"]
    .dropna()
    .str.split(";")
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)

st.bar_chart(autores)

# Palabras clave más frecuentes
st.subheader("🔑 Palabras clave más frecuentes")

keywords = (
    df_filtrado["Author Keywords"]
    .dropna()
    .str.split(";")
    .explode()
    .str.strip()
    .value_counts()
    .head(15)
)

st.bar_chart(keywords)

st.markdown("---")

st.subheader("📌 Principales hallazgos")

st.write("""
• La producción científica sobre ChatGPT y programación ha aumentado en los últimos años.

• Los artículos más citados muestran un interés creciente por la inteligencia artificial aplicada a la educación.

• Las palabras clave más frecuentes evidencian una fuerte relación entre ChatGPT, programación y aprendizaje universitario.

• Los resultados sugieren que ChatGPT es una herramienta de apoyo para el aprendizaje de programación y el desarrollo de habilidades de resolución de problemas.
""")

# Información del proyecto
st.markdown("---")
st.markdown("""
**Grupo 1**

**Pregunta de investigación:**  
¿Cómo influye el uso de ChatGPT en el aprendizaje de programación de estudiantes universitarios?
""")

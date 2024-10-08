import streamlit as st
import pandas as pd
import io
import os

# Ruta del archivo CSV
CSV_FILE = 'datos_colaboracion.csv'

# Función para cargar datos desde el archivo CSV
def load_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE).to_dict(orient='records')
    return []

# Función para guardar datos en el archivo CSV
def save_data(data):
    df = pd.DataFrame(data)
    df.to_csv(CSV_FILE, index=False)

# Inicializar la variable 'data' en session_state si no está inicializada
if 'data' not in st.session_state:
    st.session_state['data'] = load_data()

st.title("Día de Muertos en Granada 2024")

image1 = "dia de muertos2.jpg"
image2 = "niños ddm.jpg"

col1, col2 = st.columns(2)

with col1:
    st.image(image1, width=350)  
with col2:
    st.image(image2, width=500)  

page_bg_css = """
<style>
    .stApp {
        background: linear-gradient(90deg, #d1c4e9, #fff3e0); /* Gradiente de violeta claro a naranja claro */
        color: #000000; /* Color negro para el texto general para mejor legibilidad */
    }   
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# Definir el formulario para que el usuario ingrese los datos
material_options = ["papel picado", "velas", "calaveritas de azúcar", "pan de muerto"]

with st.form("Datos del usuario"):
    nombre = st.text_input("Nombre")
    material = st.selectbox('Material sugerido', sorted(material_options))
    colaboracion = st.text_input("Colaboración voluntaria")
    cantidad = st.number_input("Cantidad", min_value=0)
    inicio_horario = st.time_input("Estaré de las:")
    fin_horario = st.time_input("Hasta las:")

    # Botón para agregar los datos
    submitted = st.form_submit_button("Agregar datos")

if submitted:
    # Agregar los datos al session_state
    st.session_state['data'].append({
        "Nombre": nombre, 
        "Material sugerido": material,
        "Colaboración voluntaria": colaboracion, 
        "Cantidad": cantidad, 
        "Estaré de las:": inicio_horario, 
        "Hasta las:": fin_horario
    })
    # Guardar los datos en el archivo CSV
    save_data(st.session_state['data'])
    st.success("Datos agregados!")

# Convertir los datos en un DataFrame
df = pd.DataFrame(st.session_state['data'])

# Botón para mostrar el DataFrame
if st.button("Mostrar la lista"):
    st.write(df)

# Botón para descargar el archivo CSV
if st.button("Descargar"):
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()
    
    st.download_button(
        label="Descargar CSV",
        data=csv_data,
        file_name='datos_colaboracion.csv',
        mime='text/csv'
    )

page_bg_css = """
<style>
body {
    background: linear-gradient(90deg, rgba(255,0,150,1) 0%, rgba(0,204,255,1) 100%);
}
</style>
"""

st.markdown(page_bg_css, unsafe_allow_html=True)


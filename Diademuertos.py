import streamlit as st
import pandas as pd
from datetime import time

st.title("Dia de Muertos en Granada 2024")

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

# Inicializar la variable 'data' en session_state si no está inicializada
if 'data' not in st.session_state:
    st.session_state['data'] = []
# Crear una lista vacía para almacenar los datos
data = []

# Definir el formulario para que el usuario ingrese los datos
material = ["papel picado", "velas", "calaveritas de azucar", "pan de muerto"]

    
with st.form("Datos del usuario"):
    nombre = st.text_input("Nombre")
    material = st.selectbox('material sugerido', sorted(material))
    colaboracion = st.text_input("Colaboracion voluntaria")
    cantidad = st.number_input("cantidad", min_value=0)
    inicio_horario = st.time_input("Estare de las:")
    fin_horario = st.time_input("Hasta las:")
    
    
    # Botón para agregar los datos
    submitted = st.form_submit_button("Agregar datos")

if submitted:
        # Agregar los datos al session_state
        st.session_state['data'].append({
            "Nombre": nombre, 
            "material sugerido": material,
            "Colaboracion voluntaria": colaboracion, 
            "Cantidad": cantidad, 
            "Estaré de las:": inicio_horario, 
            "Hasta las:": fin_horario
        })
        st.success("Datos agregados!")

# Convertir los datos en un DataFrame
df = pd.DataFrame(st.session_state['data'])

# Botón para mostrar el DataFrame
if st.button("Mostrar DataFrame"):
    st.write(df)

page_bg_css = """
<style>
body {
    background: linear-gradient(90deg, rgba(255,0,150,1) 0%, rgba(0,204,255,1) 100%);
}
</style>
"""

st.markdown(page_bg_css, unsafe_allow_html=True)


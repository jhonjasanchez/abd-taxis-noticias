import streamlit as st
import pandas as pd


# Carga tus datos desde una fuente (por ejemplo, un archivo CSV)
def cargar_datos_annios():
  datos=pd.read_csv('salida_2011_1.csv',sep=",",encoding='latin-1', decimal='.')
  columna = datos['ANIO_VIAJE']
  lista_annios = columna.tolist()
  lista_annios.sort()
  return lista_annios


# Carga los datos
annios = cargar_datos_annios()


# Crear un título
st.title("¡Información de viajes de taxis!")

# Obtener la entrada del usuario
input_usuario = st.text_input("Seleccionar un año:")

# Filtrar las opciones basadas en la entrada del usuario
opciones_filtradas = [opcion for opcion in annios]

# Mostrar las opciones filtradas en el selectbox
opcion_seleccionada = st.selectbox("Selecciona un año", opciones_filtradas)
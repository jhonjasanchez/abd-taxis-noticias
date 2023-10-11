import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Carga tus datos desde una fuente (por ejemplo, un archivo CSV)
def cargar_datos_annios():
  datos=pd.read_csv('salida_2011_1.csv',sep=",",encoding='latin-1', decimal='.')
  columna = datos['ANIO_VIAJE'].unique()
  lista_annios = columna.tolist()
  lista_annios.sort()
  return lista_annios


# pintar el mapa de calor de un año
def pintar_mapa_calor(annio):
    df=pd.read_csv('salida_2011_1.csv',sep=",",encoding='latin-1', decimal='.')
    df = df.groupby(['Borough_SALIDA', 'Borough_LLEGADA'])['TOTAL_VIAJES'].sum().reset_index()
    st.write("Columnas", df.columns)
    heatmap_data = df.pivot(index='Borough_SALIDA', columns='Borough_LLEGADA', values='TOTAL_VIAJES')
    # Create a heatmap
    plt.figure(figsize=(8, 6))  # Adjust the figure size as needed

    # Use Seaborn's heatmap function
    sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt="d", linewidths=0.5)

    #plt.title("City-to-City Distance Heatmap")
    #plt.show()



# Carga los datos
annios = cargar_datos_annios()


# Crear un título
st.title("¡Información de viajes de taxis!")

# Filtrar las opciones basadas en la entrada del usuario
opciones_filtradas = [opcion for opcion in annios]

# Mostrar las opciones filtradas en el selectbox
opcion_seleccionada = st.selectbox("Selecciona un año", opciones_filtradas)

pintar_mapa_calor(2011)
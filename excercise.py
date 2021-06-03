import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

hrv = joblib.load("hrv.pkl")
hrv = pd.DataFrame(hrv)

st.title("Ejercicio práctico")
st.subheader("El objetivo de este ejercicio es que diseñes tu propio método para analizar los datos de HRV dinamicamente.")


#######################	CONSEJOS ###############################
#
# Puedes acceder a los nombres de las columnas con hrv.columns
#
# Puedes emplear st.select box para presentar opciones
st.write("__Ejemplo selectbox:__")
valor = st.selectbox("Opciones",("1era opcion","2da opcion", "..."))

st.write("Se ha seleccionado la opcion ",valor)
# Puedes emplear st.checkbox
st.write("__Ejemplo checkbox:__")
chk = st.checkbox("¿Si o No?")
if chk:
	st.write("Checkbox marcado")
else:
	st.write("Checkbox sin marcar")
#	
# Puedes consultar la api de streamlit para ver mas opciones https://docs.streamlit.io/en/stable/api.html
# 
# Y generar graficos con sns, por ejemplo:

st.write("__Ejemplo con graficos:__")

chk = st.checkbox("Añadir variable")

if chk:
	data = hrv[[  hrv.columns[2], hrv.columns[3], hrv.columns[4] ]]
	fig = sns.pairplot(data)
	st.pyplot(fig)
else:
	data = hrv[[hrv.columns[2],hrv.columns[3]]]
	fig = sns.pairplot(data)
	st.pyplot(fig)

# Ahora te toca probar, ¿puedes pensar en una forma de elegir dinamicamente variables y presentarlas en un gráfico?

st.header('___Tu Turno:___')
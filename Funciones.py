import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
 
def cargarArchivo(ruta): 
  return pd.read_csv(ruta) 

lista = []
emisiones = cargarArchivo("/Users/Carlos/ACT 03-MAY/ACTIVIDAD-03-MAY/DATOS/Emisiones_limpio.csv")

entidades = emisiones["ENTIDAD"].unique()

for i in entidades:
    lista.append(["Femenino", i, emisiones[(emisiones["SEXO"] == "Femenino") & (emisiones["ENTIDAD"] == i)]["NUMERO DE ASEGURADOS"].sum()])
    lista.append(["Masculino", i, emisiones[(emisiones["SEXO"] == "Masculino") & (emisiones["ENTIDAD"] == i)]["NUMERO DE ASEGURADOS"].sum()])

new_df = pd.DataFrame(lista, columns=["SEXO", "ENTIDAD", "OCURRENCIAS"])

fig = px.bar(new_df, x="ENTIDAD", y="OCURRENCIAS", color="SEXO", barmode="group", 
             title="Número de asegurados por entidad y sexo")
fig.update_layout(xaxis_title="", yaxis_title="Número de asegurados", legend_title="")
fig.show()





comisiones = cargarArchivo("/Users/Carlos/ACT 03-MAY/ACTIVIDAD-03-MAY/DATOS/Comisiones_limpio.csv")

# Definimos una lista vacía
lista = []

# Obtenemos las diferentes modalidades de poliza
polizas = comisiones["MODALIDAD DE LA POLIZA"].unique()

# Agrupamos los datos por sexo y modalidad de poliza
for i in polizas:
    # Agrupamos los datos por sexo en Femenino
    lista.append(["Femenino", i, comisiones[(comisiones["SEXO"] == "Femenino") & (comisiones["MODALIDAD DE LA POLIZA"] == i)]["NUMERO DE ASEGURADOS"].sum()])
    # Agrupamos los datos por sexo en Masculino
    lista.append(["Masculino", i, comisiones[(comisiones["SEXO"] == "Masculino") & (comisiones["MODALIDAD DE LA POLIZA"] == i)]["NUMERO DE ASEGURADOS"].sum()])

# Creamos un nuevo DataFrame con nuestra lista de valores
new_df = pd.DataFrame(lista, columns=["SEXO", "MODALIDAD DE LA POLIZA", "OCURRENCIAS"]) 

# Creamos un gráfico de barras utilizando el método Bar de plotly.graph_objs
fig = go.Figure()
for gender in new_df['SEXO'].unique():
    fig.add_trace(go.Bar(x=new_df[new_df['SEXO']==gender]['MODALIDAD DE LA POLIZA'], 
                         y=new_df[new_df['SEXO']==gender]['OCURRENCIAS'], 
                         name=gender))

fig.update_layout(title="Número de asegurados por modalidad de poliza y sexo",
                  xaxis_title="MODALIDAD DE LA POLIZA",
                  yaxis_title="OCURRENCIAS")

fig.show()
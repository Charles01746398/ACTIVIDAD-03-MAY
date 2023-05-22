import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html

def cargarArchivo(ruta): 
    return pd.read_csv(ruta)
 

emisiones = cargarArchivo("DATOS/Emisiones_limpio.csv")

print(emisiones.head())

entidades = emisiones["ENTIDAD"].unique()

lista_entidades = []

for i in entidades:
    lista_entidades.append(["Femenino", i, emisiones[(emisiones["SEXO"] == "Femenino") & (emisiones["ENTIDAD"] == i)]["NUMERO DE ASEGURADOS"].sum()])
    lista_entidades.append(["Masculino", i, emisiones[(emisiones["SEXO"] == "Masculino") & (emisiones["ENTIDAD"] == i)]["NUMERO DE ASEGURADOS"].sum()])

df_entidades = pd.DataFrame(lista_entidades, columns=["SEXO", "ENTIDAD", "OCURRENCIAS"]) 

fig_entidades = px.bar(df_entidades, x="ENTIDAD", y="OCURRENCIAS", color="SEXO", barmode="group", 
             title="Número de asegurados por entidad y sexo")
fig_entidades.update_layout(xaxis_title="", yaxis_title="Número de asegurados", legend_title="")

comisiones = cargarArchivo("DATOS/Comisiones_limpio.csv")

polizas = comisiones["MODALIDAD DE LA POLIZA"].unique()

lista_polizas = []

for i in polizas:
    lista_polizas.append(["Femenino", i, comisiones[(comisiones["SEXO"] == "Femenino") & (comisiones["MODALIDAD DE LA POLIZA"] == i)]["NUMERO DE ASEGURADOS"].sum()])
    lista_polizas.append(["Masculino", i, comisiones[(comisiones["SEXO"] == "Masculino") & (comisiones["MODALIDAD DE LA POLIZA"] == i)]["NUMERO DE ASEGURADOS"].sum()])


df_polizas = pd.DataFrame(lista_polizas, columns=["SEXO", "MODALIDAD DE LA POLIZA", "OCURRENCIAS"]) 


fig_polizas = go.Figure

import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

# Cargar los datos
emisiones = pd.read_csv("DATOS/Emisiones_limpio.csv")
comisiones = pd.read_csv("DATOS/Comisiones_limpio.csv")

# Crear la aplicación de Dash
app = dash.Dash(__name__)

# Crear el layout
app.layout = html.Div(children=[
    html.H1(children='Número de asegurados por entidad y sexo'),
    dcc.Graph(
        id='entidades',
        figure=px.bar(df_entidades, x="ENTIDAD", y="OCURRENCIAS", color="SEXO", barmode="group", 
                      title="Número de asegurados por entidad y sexo")
    ),
    html.H1(children='Número de asegurados por modalidad de la póliza y sexo'),
    dcc.Graph(
        id='polizas',
        figure=px.bar(df_polizas, x="MODALIDAD DE LA POLIZA", y="OCURRENCIAS", color="SEXO", barmode="group", 
                      title="Número de asegurados por modalidad de la póliza y sexo")
    )
])

# Iniciar la aplicación de Dash
if __name__ == '__main__':
    app.run_server(debug=True)



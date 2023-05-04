import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

df_Comisiones_limpio = pd.read_csv('Comisiones_limpio.csv')

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Comisiones de seguros'),

    html.Div(children='''
        Visualización de datos de comisiones de seguros.
    '''),

    dcc.Graph(
        id='grafico-prima-cedida',
        figure={
            'data': [
                {'x': df_Comisiones_limpio['FECHA DE EMISION'], 'y': df_Comisiones_limpio['PRIMA CEDIDA'], 'type': 'bar', 'name': 'Prima cedida'},
            ],
            'layout': {
                'title': 'Prima cedida'
            }
        }
    ),

    dcc.Graph(
        id='grafico-comisiones-fondos',
        figure={
            'data': [
                {'x': df_Comisiones_limpio['FECHA DE EMISION'], 'y': df_Comisiones_limpio['COMISIONES DIRECTAS'], 'type': 'bar', 'name': 'Comisiones directas'},
                {'x': df_Comisiones_limpio['FECHA DE EMISION'], 'y': df_Comisiones_limpio['FONDO DE INVERSIÓN'], 'type': 'bar', 'name': 'Fondo de inversión'},
                {'x': df_Comisiones_limpio['FECHA DE EMISION'], 'y': df_Comisiones_limpio['FONDO DE ADMINISTRACION'], 'type': 'bar', 'name': 'Fondo de administración'}
            ],
            'layout': {
                'title': 'Comisiones directas y fondos'
            },
            'barmode': 'stack'
        }
    ),
    
    dcc.Graph(
        id='grafico-numero-asegurados-rescate',
        figure={
            'data': [
                {'x': df_Comisiones_limpio['FECHA DE EMISION'], 'y': df_Comisiones_limpio['NUMERO DE ASEGURADOS'], 'type': 'line', 'name': 'Número de asegurados'},
                {'x': df_Comisiones_limpio['FECHA DE EMISION'], 'y': df_Comisiones_limpio['MONTO DE RESCATE'], 'type': 'line', 'name': 'Monto de rescate'}
            ],
            'layout': {
                'title': 'Número de asegurados y monto de rescate'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

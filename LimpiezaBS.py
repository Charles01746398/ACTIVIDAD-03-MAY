import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df_Emisiones_limpio = pd.read_csv("Emisiones_limpio.csv")

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Emisiones de seguros'),

    html.Div(children='''
        Visualización de datos de emisiones de seguros.
    '''),

    dcc.Graph(
        id='grafico-emisiones',
        figure={
            'data': [
                {'x': df_Emisiones_limpio['FECHA EMISION'], 'y': df_Emisiones_limpio['PRIMA EMITIDA'], 'type': 'line', 'name': 'Prima emitida'},
                {'x': df_Emisiones_limpio['FECHA EMISION'], 'y': df_Emisiones_limpio['NUMERO DE ASEGURADOS'], 'type': 'bar', 'name': 'Número de asegurados'},
                {'x': df_Emisiones_limpio['FECHA EMISION'], 'y': df_Emisiones_limpio['SUMA ASEGURADA'], 'type': 'bar', 'name': 'Suma asegurada'}
            ],
            'layout': {
                'title': 'Emisiones de seguros'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
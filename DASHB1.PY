import dash
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go

datos = pd.read_csv('/Users/Carlos/ACT 03-MAY/ACTIVIDAD-03-MAY/DATOS/Siniestros_limpio.csv')

top_causas = datos['CAUSA DEL SINIESTRO'].value_counts().nlargest(15)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='grafico-dinamico')
])

@app.callback(
    Output('grafico-dinamico', 'figure'),
    [Input('grafico-dinamico', 'n_intervals')]
)
def update_graph(n):
    top_causas_actualizado = top_causas.head(n)

    figura = {
        'data': [
            {'x': top_causas_actualizado.index, 'y': top_causas_actualizado.values, 'type': 'bar'}
        ],
        'layout': {
            'title': 'Top 15 de Causa del Siniestro',
            'xaxis': {'title': 'Causa'},
            'yaxis': {'title': 'Cantidad'}
        }
    }

    return figura

if __name__ == '__main__':
    app.run_server(debug=True)

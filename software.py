import pandas as pd
import sqlalchemy
import plotly.express as px
import dash
from dash import dash_table
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from datetime import date
import plotly.graph_objs as go

import json

# Leitura da base de dados
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root@localhost/cio_database')
softwares = pd.read_sql_table('softwares', engine)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Row([
                html.P("Tipos de manutenção"),
                dcc.Dropdown(
                    id='manutencao',
                    options=[{'value': x, 'label': x}
                             for x in ['Corretivas', 'Adaptativas', 'Perfectivas']],
                    clearable=True
                )
            ]),
            dbc.Row([
                html.P("Softwares da Empresa"),
                dcc.Dropdown(
                    id='softwares_da_empresa',
                    options=[{'value': x, 'label': x}
                             for x in ['Caixa Mobile', 'CaixaNet', 'Microcredit', 'Digital Credit', 'Site da Caixa']],
                    clearable=True
                )
            ]),
            dbc.Row([html.P("Data dos Updates"),
                     dcc.Dropdown(
                id='data',
                options=[{'value': '1', 'label': 'janeiro'},
                         {'value': '2', 'label': 'fevereiro'},
                         {'value': '3', 'label': 'março'},
                         {'value': '4', 'label': 'abril'},
                         {'value': '5', 'label': 'maio'},
                         {'value': '6', 'label': 'junho'},
                         {'value': '7', 'label': 'julho'},
                         {'value': '8', 'label': 'agosto'},
                         {'value': '9', 'label': 'setembro'},
                         {'value': '10', 'label': 'outubro'},
                         {'value': '11', 'label': 'novembro'},
                         {'value': '12', 'label': 'dezembro'}, ],
                clearable=True
            )])
        ], width=2),
        dbc.Col([
            dbc.Row([
                dcc.Graph(id="barra_1")
                ]),
            dbc.Row([
                dcc.Graph(id="barra_2")
                ]),
            dbc.Row([
                dcc.Graph(id="barra_3")
                ])
            ], width=6),
        dbc.Col([
            dbc.Row([
                dbc.Card([
                    dbc.CardBody([
                        html.H2(id="custo", children="",
                                style={'fontWeight': 'bold'}),
                        html.H5("Custo")
                    ])
                ])
            ]),
            dbc.Row([
                dcc.Graph(id="pie-chart_1")
                ]),
            dbc.Row([
                dcc.Graph(id="pie-chart_2")
                ])
        ], width=4)
    ])
])

@ app.callback(
    Output("custo", "children"),
    [Input("manutencao", "value"),
     Input("softwares_da_empresa", "value"),
     Input("data", "value"), ]
)
def generate_chart(manutencao, softwares_da_empresa, data):
    if (manutencao is None):
        valor2 = softwares
    else:
        valor = softwares['Tipos de manutencao'] == manutencao
        valor2 = softwares[valor]

    if (softwares_da_empresa is None):
        valor2 = valor2
    else:
        valor = valor2['Softwares da Empreza'] == softwares_da_empresa
        valor2 = valor2[valor]
    
    if (data is None):
        valor2 = valor2
    else:
        valor = valor2['mes das manutencoes'] == data
        valor2 = valor2[valor]
        
    return valor2['Custo'].sum()

@ app.callback(
    Output("barra_1", "figure"),
    [Input("manutencao", "value"),
     Input("softwares_da_empresa", "value"),
     Input("data", "value"), ]
)
def generate_chart(manutencao, softwares_da_empresa, data):
    if (manutencao is None):
        valor2 = softwares
    else:
        valor = softwares['Tipos de manutencao'] == manutencao
        valor2 = softwares[valor]

    if (softwares_da_empresa is None):
        valor2 = valor2
    else:
        valor = valor2['Softwares da Empreza'] == softwares_da_empresa
        valor2 = valor2[valor]
    
    if (data is None):
        valor2 = valor2
    else:
        valor = valor2['mes das manutencoes'] == data
        valor2 = valor2[valor]
        
    fig={
        'data': [
            {'x': valor2['Tipos de manutencao'], 'y': valor2['Custo'], 'type': 'bar'}
        ],
        'layout': {
            'title': 'Custo das Manutencoes'
        }
    }

    return fig

@ app.callback(
    Output("barra_2", "figure"),
    [Input("manutencao", "value"),
     Input("softwares_da_empresa", "value"),
     Input("data", "value"), ]
)
def generate_chart(manutencao, softwares_da_empresa, data):
    if (manutencao is None):
        valor2 = softwares
    else:
        valor = softwares['Tipos de manutencao'] == manutencao
        valor2 = softwares[valor]

    if (softwares_da_empresa is None):
        valor2 = valor2
    else:
        valor = valor2['Softwares da Empreza'] == softwares_da_empresa
        valor2 = valor2[valor]
    
    if (data is None):
        valor2 = valor2
    else:
        valor = valor2['mes das manutencoes'] == data
        valor2 = valor2[valor]
        
    fig={
        'data': [
            {'x': valor2['Softwares da Empreza'], 'y': valor2['Custo'], 'type': 'bar'}
        ],
        'layout': {
            'title': 'Custo dos Softwares'
        }
    }

    return fig

@ app.callback(
    Output("barra_3", "figure"),
    [Input("manutencao", "value"),
     Input("softwares_da_empresa", "value"),
     Input("data", "value"), ]
)
def generate_chart(manutencao, softwares_da_empresa, data):
    if (manutencao is None):
        valor2 = softwares
    else:
        valor = softwares['Tipos de manutencao'] == manutencao
        valor2 = softwares[valor]

    if (softwares_da_empresa is None):
        valor2 = valor2
    else:
        valor = valor2['Softwares da Empreza'] == softwares_da_empresa
        valor2 = valor2[valor]
    
    if (data is None):
        valor2 = valor2
    else:
        valor = valor2['mes das manutencoes'] == data
        valor2 = valor2[valor]
        
    fig={
        'data': [
            {'x': valor2['mes das manutencoes'], 'y': valor2['Custo'], 'type': 'bar'}
        ],
        'layout': {
            'title': 'Custo Mensal'
        }
    }

    return fig

@ app.callback(
    Output("pie-chart_1", "figure"),
    [Input("manutencao", "value"),
     Input("softwares_da_empresa", "value"),
     Input("data", "value"), ]
)
def generate_chart(manutencao, softwares_da_empresa, data):
    if (manutencao is None):
        valor2 = softwares
    else:
        valor = softwares['Tipos de manutencao'] == manutencao
        valor2 = softwares[valor]

    if (softwares_da_empresa is None):
        valor2 = valor2
    else:
        valor = valor2['Softwares da Empreza'] == softwares_da_empresa
        valor2 = valor2[valor]
    
    if (data is None):
        valor2 = valor2
    else:
        valor = valor2['mes das manutencoes'] == data
        valor2 = valor2[valor]
    
    fig = px.pie(valor2, values='Custo', names='Tipos de manutencao',hole=.6)

    return fig

@ app.callback(
    Output("pie-chart_2", "figure"),
    [Input("manutencao", "value"),
     Input("softwares_da_empresa", "value"),
     Input("data", "value"), ]
)
def generate_chart(manutencao, softwares_da_empresa, data):
    if (manutencao is None):
        valor2 = softwares
    else:
        valor = softwares['Tipos de manutencao'] == manutencao
        valor2 = softwares[valor]

    if (softwares_da_empresa is None):
        valor2 = valor2
    else:
        valor = valor2['Softwares da Empreza'] == softwares_da_empresa
        valor2 = valor2[valor]
    
    if (data is None):
        valor2 = valor2
    else:
        valor = valor2['mes das manutencoes'] == data
        valor2 = valor2[valor]
  
    fig = px.pie(valor2, values='Custo', names='Softwares da Empreza',hole=.6)


    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

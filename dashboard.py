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
    'mysql+pymysql://root:Kevin580p&@127.0.0.1:3306/ciomanutencao')

cio = pd.merge(pd.read_sql_table('equipamentos', engine), pd.read_sql_table(
    'caixa_manutencao', engine), on="codigo do equipamento", how="outer")


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([

    dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.P("Dispositivos da Empresa"),
                    dcc.Dropdown(
                        id='dispositivos',
                        options=[{'value': x, 'label': x}
                                 for x in ['Cofre', 'Reciclador de dinheiro', 'Contador de moedas', 'contador de notas',
                                           'Computador', 'Impressora', 'router', 'switch', 'Mouse', 'Teclado', 'Monitor', 'Ar-Condicionado']],
                        clearable=True
                    )
                ]),
                dbc.Row([
                    html.P("Agencias"),
                    dcc.Dropdown(
                        id='agencias',
                        options=[{'value': x, 'label': x}
                                 for x in ['Achada S. Filipe', 'Achada Sto. António', 'Aeroporto da Praia', 'Centro Comercial Sucupira',
                                           'Fazenda', 'Palmarejo', 'Sede', 'Plato']],
                        clearable=True
                    )
                ]),
                dbc.Row([
                    html.P("Estado dos Equipamentos"),
                    dcc.Dropdown(
                        id='estado',
                        options=[{'value': x, 'label': x}
                                 for x in ['funcionando', 'danificado']],
                        clearable=True
                    )
                ]),
                dbc.Row([
                    html.P("Data de Requisição"),
                    dcc.Dropdown(
                        id='data',
                        options=[{'value': 1, 'label': 'janeiro'},
                                 {'value': 2, 'label': 'fevereiro'},
                                 {'value': 3, 'label': 'março'},
                                 {'value': 4, 'label': 'abril'},
                                 {'value': 5, 'label': 'maio'},
                                 {'value': 6, 'label': 'junho'},
                                 {'value': 7, 'label': 'julho'},
                                 {'value': 8, 'label': 'agosto'},
                                 {'value': 9, 'label': 'setembro'},
                                 {'value': 10, 'label': 'outubro'},
                                 {'value': 11, 'label': 'novembro'},
                                 {'value': 12, 'label': 'dezembro'}, ],
                        clearable=True
                    )
                ])
            ], width=2),
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H2(id="total_de_equipamentos", children="",
                                        style={'fontWeight': 'bold'}),
                                html.H5("Total de equipamentos")
                            ])
                        ])
                    ]),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H2(id="manutencao_equipamentos", children="",
                                        style={'fontWeight': 'bold'}),
                                html.H5(
                                    "Equipamentos que foram para a manutenção")
                            ])
                        ])
                    ]),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H2(id="total_reparação", children="",
                                        style={'fontWeight': 'bold'}),
                                html.H5("custo de reparacao")
                            ])
                        ])
                    ])
                ]),
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id="barra")
                    ]),
                    dbc.Col([
                        dbc.Row([
                            dcc.Graph(id="pie-chart_1")
                        ]),
                        dbc.Row([
                            dcc.Graph(id="pie-chart_2")
                        ])
                    ])
                ])
            ], width=10)
            ])

])


@ app.callback(
    Output("total_de_equipamentos", "children"),
    [Input("dispositivos", "value"),
     Input("agencias", "value"),
     Input("estado", "value"),
     Input("data", "value"), ]
)
def generate_chart(dispositivos, agencias, estado, data):
    cio2 = cio.groupby(['Nome do Produto', 'Agencias',
                       'estado do equipamento', 'Data da requisicao']).mean()

    if (dispositivos is None):
        valor2 = cio
    else:
        valor = cio['Nome do Produto'] == dispositivos
        valor2 = cio[valor]

    if (agencias is None):
        valor2 = valor2
    else:
        valor = valor2['Agencias'] == agencias
        valor2 = valor2[valor]

    if (estado is None):
        valor2 = valor2

    else:
        valor = valor2['estado do equipamento'] == estado
        valor2 = valor2[valor]

    if (data is None):
        valor2 = valor2

    else:
        valor = valor2['mes da requisicao'] == data
        valor2 = valor2[valor]

    x = len(valor2)
    return x


@ app.callback(
    Output("manutencao_equipamentos", "children"),
    [Input("dispositivos", "value"),
     Input("agencias", "value"),
     Input("estado", "value"),
     Input("data", "value"), ]
)
def generate_chart(dispositivos, agencias, estado, data):

    values = ['concluido', 'em aberto', 'cancelado']
    cio2 = cio[cio.status.isin(values)]

    if (dispositivos is None):
        valor2 = cio2
    else:
        valor = cio2['Nome do Produto'] == dispositivos
        valor2 = cio2[valor]

    if (agencias is None):
        valor2 = valor2
    else:
        valor = valor2['Agencias'] == agencias
        valor2 = valor2[valor]

    if (estado is None):
        valor2 = valor2

    else:
        valor = valor2['estado do equipamento'] == estado
        valor2 = valor2[valor]

    if (data is None):
        valor2 = valor2

    else:
        valor = valor2['mes da requisicao'] == data
        valor2 = valor2[valor]

    x = len(valor2)
    return x


@ app.callback(
    Output("total_reparação", "children"),
    [Input("dispositivos", "value"),
     Input("agencias", "value"),
     Input("estado", "value"),
     Input("data", "value")]
)
def generate_chart(dispositivos, agencias, estado, data):

    if (dispositivos is None):
        valor2 = cio
    else:
        valor = cio['Nome do Produto'] == dispositivos
        valor2 = cio[valor]

    if (agencias is None):
        valor2 = valor2
    else:
        valor = valor2['Agencias'] == agencias
        valor2 = valor2[valor]

    if (estado is None):
        valor2 = valor2

    else:
        valor = valor2['estado do equipamento'] == estado
        valor2 = valor2[valor]

    if (data is None):
        valor2 = valor2

    else:
        valor = valor2['mes da requisicao'] == data
        valor2 = valor2[valor]

    return valor2['custo de reparacao'].sum()


@ app.callback(
    Output("pie-chart_1", "figure"),
    [Input("dispositivos", "value"),
     Input("agencias", "value"),
     Input("estado", "value"),
     Input("data", "value")])
def generate_chart(dispositivos, agencias, estado, data):
    if (dispositivos is None):
        valor2 = cio
    else:
        valor = cio['Nome do Produto'] == dispositivos
        valor2 = cio[valor]

    if (agencias is None):
        valor2 = valor2
    else:
        valor = valor2['Agencias'] == agencias
        valor2 = valor2[valor]

    if (estado is None):
        valor2 = valor2

    else:
        valor = valor2['estado do equipamento'] == estado
        valor2 = valor2[valor]

    if (data is None):
        valor2 = valor2

    else:
        valor = valor2['mes da requisicao'] == data
        valor2 = valor2[valor]

    fig = px.pie(valor2, values='custo de reparacao', names='Nome do Produto')

    return fig


@ app.callback(
    Output("pie-chart_2", "figure"),
    [Input("dispositivos", "value"),
     Input("agencias", "value"),
     Input("estado", "value"),
     Input("data", "value")])
def generate_chart(dispositivos, agencias, estado, data):

    if (dispositivos is None):
        valor2 = cio
    else:
        valor = cio['Nome do Produto'] == dispositivos
        valor2 = cio[valor]

    if (agencias is None):
        valor2 = valor2
    else:
        valor = valor2['Agencias'] == agencias
        valor2 = valor2[valor]

    if (estado is None):
        valor2 = valor2

    else:
        valor = valor2['estado do equipamento'] == estado
        valor2 = valor2[valor]

    if (data is None):
        valor2 = valor2

    else:
        valor = valor2['mes da requisicao'] == data
        valor2 = valor2[valor]

    fig = px.pie(valor2, values=valor2.value_counts(
        ['codigo do equipamento']).values, names=valor2['estado do equipamento'])

    return fig


@ app.callback(
    Output("barra", "figure"),
    [Input("dispositivos", "value"),
     Input("agencias", "value"),
     Input("estado", "value"),
     Input("data", "value")])
def generate_chart(dispositivos, agencias, estado, data):

    if (dispositivos is None):
        valor2 = cio
    else:
        valor = cio['Nome do Produto'] == dispositivos
        valor2 = cio[valor]

    if (agencias is None):
        valor2 = valor2
    else:
        valor = valor2['Agencias'] == agencias
        valor2 = valor2[valor]

    if (estado is None):
        valor2 = valor2

    else:
        valor = valor2['estado do equipamento'] == estado
        valor2 = valor2[valor]

    if (data is None):
        valor2 = valor2

    else:
        valor = valor2['mes da requisicao'] == data
        valor2 = valor2[valor]

    valor = valor2['estado do equipamento'] == 'funcionando'
    valorx = valor2[valor]
    valor = valor2['estado do equipamento'] == 'danificado'
    valory = valor2[valor]

    fig = {
        'data': [
            {'x': valorx['Nome do Produto'], 'y': valorx.value_counts(
                ['codigo do equipamento']), 'type': 'bar', 'name': 'funcionando'},
            {'x': valory['Nome do Produto'], 'y': valory.value_counts(
                ['codigo do equipamento']), 'type': 'bar', 'name': 'danificado'},
        ],
        'layout': {
            'title': 'Numero de Equipamentos',
        },


    }

    return fig

# 46B648


if __name__ == '__main__':
    app.run_server(debug=True)

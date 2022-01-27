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


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# importando a base de dados
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:Kevin580p&@127.0.0.1:3306/cio_manutencao')

df = pd.read_sql_table('requisicoes', engine)
""" df = pd.read_sql_query('SELECT `Nome do Produto` From requisicoes',engine)
print(df) """

dh = pd.read_sql_table('equipamentos', engine)

teste = pd.merge(pd.read_sql_table('equipamentos', engine), pd.read_sql_table(
    'requisicoes', engine), on="codigo do equipamento", how="outer")


""" fig = px.pie(df, values='custo de reparação', names='Tipo de Manutenção')
fig.show() """

""" app.layout = dash_table.DataTable(
    data=teste.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in {"Agências","Nome do Produto","estado do equipamento","status"}],
    page_action='none',
    style_table={'height': '300px', 'overflowY': 'auto'}
) """


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H2(id="Nome do produto", children="",
                            style={'fontWeight': 'bold'}),
                    html.H5("Total de equipamentos")
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H2(id="codigo do equipamento", children="",
                            style={'fontWeight': 'bold'}),
                    html.H5("Equipamentos que foram para a manutenção")
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H2(id="custo de reparação", children="",
                            style={'fontWeight': 'bold'}),
                    html.H5("Custo de reparação")
                ])
            ])
        ], width=6)
    ], className="mb-3"),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                },
                style_cell={'textAlign': 'left'},
                data=teste.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in {"Agências",
                                                        "Nome do Produto", "estado do equipamento", "status"}],
                fixed_rows={'headers': True},
                page_action='none',
                style_table={'height': '300px', 'overflowY': 'auto'}
            )
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.P("Nome:"),
            dcc.Dropdown(
                id='names',
                value='Nome do Produto',
                options=[{'value': x, 'label': x}
                         for x in ['Nome do Produto', 'Agências']],

                clearable=False
            )
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.P("Estado dos equipamentos"),
            dcc.Dropdown(
                id='equipamentos',
                value='estado do equipamento',
                options=[{'value': x, 'label': x}
                         for x in ['estado do equipamento']],

                clearable=False
            )
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="pie-chart_1")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="pie-chart")
        ])
    ])
])


@app.callback(
    Output("pie-chart_1", "figure"),
    [Input("names", "value")])
def generate_chart(names):
    fig = px.pie(teste, values='custo de reparação', names=names)
    return fig


@app.callback(
    Output("pie-chart", "figure"),
    [Input("equipamentos", "value")]
)
def generate_chart(names):
    fig = px.pie(teste, values='custo de reparação', names=names)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

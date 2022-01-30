import pandas as pd
import sqlalchemy
import plotly.express as px
import dash
from dash import dash_table
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
# import dash_bootstrap_components as dbc
from datetime import date
import plotly.graph_objs as go


import json


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)


# importando a base de dados
# engine = sqlalchemy.create_engine(
#     'cio')

equipamentos = pd.read_sql_table('equipamentos','sqlite:///cio.db')
requisicoes = pd.read_sql_table('requisicoes','sqlite:///cio.db')

teste = pd.merge(equipamentos, requisicoes, on="codigoEquipamento", how="outer")

html.H2(id="nomeProduto", children= "",
        style={'fontWeight': 'bold'}),
html.H5("Total de equipamentos")

html.H2(id="codigoEquipamento", children="",
        style={'fontWeight': 'bold'}),
html.H5("Equipamentos que foram para a manutenção")

html.H2(id="custoReparação", children="",
        style={'fontWeight': 'bold'}),
html.H5("Custo de reparação")

dash_table.DataTable(
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    },
    style_cell={'textAlign': 'left'},
    data=teste.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in {"agencias",
                                            "nomeProduto", "estadoEquipamento", "status"}],
    fixed_rows={'headers': True},
    page_action='none',
    style_table={'height': '300px', 'overflowY': 'auto'}
)

dcc.Dropdown(
    id='names',
    value='nomeProduto',
    options=[{'value': x, 'label': x}
             for x in ['nomeProduto', 'agencias']],

    clearable=False
)

html.P("Estado dos equipamentos"),
dcc.Dropdown(
    id='equipamentos',
    value='estadoEquipamento',
    options=[{'value': x, 'label': x}
             for x in ['estadoEquipamento']],
    clearable=False
)

dcc.Graph(id="pie-chart_1")

dcc.Graph(id="pie-chart")


@app.callback(
    Output("pie-chart_1", "figure"),
    [Input("names", "value")])
def generate_chart(names):
    fig = px.pie(teste, values='custoReparacao', names=names)
    return fig


@app.callback(
    Output("pie-chart", "figure"),
    [Input(equipamentos, "value")])
def generate_chart(names):
    fig = px.pie(teste, values='custoReparacao', names=names)
    return fig

@app.callback(
    Output("codigoEquipamento", "children"),
    [Input("names", "value")]
)
# def generate_chart(names):
#     x = len(requisicoes)
#     return x

@app.callback(
    Output("nomeProduto", "children"),
    [Input("names", "value")]
)
def generate_chart(names):
    x = len(equipamentos)
    return x


#result = PessoModel.query.fliter_by(id=pesso)


if __name__ == '__main__':
    app.run_server(debug=True)

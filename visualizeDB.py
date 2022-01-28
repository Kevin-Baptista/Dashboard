import pandas as pd

equipamentos = pd.read_sql_table('equipamentos','sqlite:///cio.db')
requisicoes = pd.read_sql_table('requisicoes','sqlite:///cio.db')
i =0
while equipamentos.values[i][3]:
    if equipamentos.values[i][0] in requisicoes:
        print(equipamentos.values[i])


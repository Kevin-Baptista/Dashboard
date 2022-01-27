import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,create_engine,types
meta = MetaData()

engine = create_engine('sqlite:///cio.db', echo= True)
equipamentos = Table(
    'equipamentos', meta,
    Column('codigoEquipamento', Integer, primary_key = True),
    Column('nomeProduto', String,nullable=False),
    Column('agencias', String,nullable=False),
    Column('estadoEquipamento',String,nullable=False)
)

requisicoes = Table(
    'requisicoes',meta,
    Column('codigoRequisicoes', Integer, primary_key=True),
    Column('dataRequisisoes',types.DateTime(),nullable=False),
    Column('tipoManutencao',String(10),nullable=False),
    Column('dataConclusao',types.DateTime(),nullable=False),
    Column('status',String(9),nullable=False),
    Column('codigoEquipamento',ForeignKey('equipamentos.codigoEquipamento')),
    Column('custoReparacao',String(13),nullable=False)
)

meta.create_all(engine)

values = [(1001, 'Cofre', 'Achada S. Filipe', 'funcionando'),
(1002, 'Cofre', 'Achada Sto. António', 'funcionando'),
(1003, 'Cofre', 'Aeroporto da Praia', 'funcionando'),
(1004, 'Cofre', 'Centro Comercial Sucupira', 'funcionando'),
(1005, 'Cofre', 'Fazenda', 'funcionando'),
(1006, 'Cofre', 'Palmarejo', 'funcionando'),
(1007, 'Cofre', 'Sede', 'funcionando'),
(1008, 'Cofre', 'Plato', 'funcionando'),
(1101, 'Reciclador de dinheiro', 'Achada S. Filipe', 'funcionando'),
(1102, 'Reciclador de dinheiro', 'Achada Sto. António', 'funcionando'),
(1103, 'Reciclador de dinheiro', 'Aeroporto da Praia', 'funcionando'),
(1104, 'Reciclador de dinheiro', 'Centro Comercial Sucupira', 'funcionando'),
(1105, 'Reciclador de dinheiro', 'Fazenda', 'danificado'),
(1106, 'Reciclador de dinheiro', 'Palmarejo', 'funcionando'),
(1107, 'Reciclador de dinheiro', 'Sede', 'funcionando'),
(1108, 'Reciclador de dinheiro', 'Plato', 'funcionando'),
(1201, 'Contador de moedas', 'Achada S. Filipe', 'funcionando'),
(1202, 'Contador de moedas', 'Achada S. Filipe', 'funcionando'),
(1203, 'Contador de moedas', 'Achada S. Filipe', 'funcionando'),
(1204, 'Contador de moedas', 'Achada Sto. António', 'funcionando'),
(1205, 'Contador de moedas', 'Achada Sto. António', 'funcionando'),
(1206, 'Contador de moedas', 'Achada Sto. António', 'funcionando'),
(1207, 'Contador de moedas', 'Aeroporto da Praia', 'funcionando'),
(1208, 'Contador de moedas', 'Centro Comercial Sucupira', 'funcionando'),
(1209, 'Contador de moedas', 'Centro Comercial Sucupira', 'funcionando'),
(1210, 'Contador de moedas', 'Centro Comercial Sucupira', 'funcionando'),
(1211, 'Contador de moedas', 'Fazenda', 'funcionando'),
(1212, 'Contador de moedas', 'Fazenda', 'funcionando'),
(1213, 'Contador de moedas', 'Fazenda', 'funcionando'),
(1214, 'Contador de moedas', 'Palmarejo', 'funcionando'),
(1215, 'Contador de moedas', 'Palmarejo', 'funcionando'),
(1216, 'Contador de moedas', 'Palmarejo', 'funcionando'),
(1217, 'Contador de moedas', 'Sede', 'funcionando'),
(1218, 'Contador de moedas', 'Sede', 'funcionando'),
(1219, 'Contador de moedas', 'Sede', 'funcionando'),
(1220, 'Contador de moedas', 'Sede', 'funcionando'),
(1221, 'Contador de moedas', 'Plato', 'funcionando'),
(1222, 'Contador de moedas', 'Plato', 'funcionando'),
(1223, 'Contador de moedas', 'Plato', 'funcionando'),
(1224, 'Contador de moedas', 'Plato', 'funcionando'),
(1225, 'Contador de moedas', 'Plato', 'funcionando'),
(1301, 'contador de notas', 'Achada S. Filipe', 'funcionando'),
(1302, 'contador de notas', 'Achada S. Filipe', 'danificado'),
(1303, 'contador de notas', 'Achada S. Filipe', 'funcionando'),
(1304, 'contador de notas', 'Achada Sto. António', 'funcionando'),
(1305, 'contador de notas', 'Achada Sto. António', 'funcionando'),
(1306, 'contador de notas', 'Achada Sto. António', 'funcionando'),
(1307, 'contador de notas', 'Aeroporto da Praia', 'funcionando'),
(1308, 'contador de notas', 'Centro Comercial Sucupira', 'funcionando'),
(1309, 'contador de notas', 'Centro Comercial Sucupira', 'funcionando'),
(1310, 'contador de notas', 'Centro Comercial Sucupira', 'funcionando'),
(1311, 'contador de notas', 'Fazenda', 'funcionando'),
(1312, 'contador de notas', 'Fazenda', 'funcionando'),
(1313, 'contador de notas', 'Fazenda', 'funcionando'),
(1314, 'contador de notas', 'Palmarejo', 'funcionando'),
(1315, 'contador de notas', 'Palmarejo', 'funcionando'),
(1316, 'contador de notas', 'Palmarejo', 'funcionando'),
(1317, 'contador de notas', 'Sede', 'funcionando'),
(1318, 'contador de notas', 'Sede', 'danificado'),
(1319, 'contador de notas', 'Sede', 'funcionando'),
(1320, 'contador de notas', 'Sede', 'funcionando'),
(1321, 'contador de notas', 'Plato', 'funcionando'),
(1322, 'contador de notas', 'Plato', 'funcionando'),
(1323, 'contador de notas', 'Plato', 'funcionando'),
(1324, 'contador de notas', 'Plato', 'danificado'),
(1325, 'contador de notas', 'Plato', 'funcionando'),
(1401, 'Computador', 'Achada S. Filipe', 'funcionando'),
(1402, 'Computador', 'Achada S. Filipe', 'funcionando'),
(1403, 'Computador', 'Achada S. Filipe', 'funcionando'),
(1404, 'Computador', 'Achada S. Filipe', 'funcionando'),
(1405, 'Computador', 'Achada Sto. António', 'funcionando'),
(1406, 'Computador', 'Achada Sto. António', 'funcionando'),
(1407, 'Computador', 'Achada Sto. António', 'funcionando'),
(1408, 'Computador', 'Achada Sto. António', 'danificado'),
(1409, 'Computador', 'Achada Sto. António', 'funcionando'),
(1410, 'Computador', 'Centro Comercial Sucupira', 'funcionando'),
(1411, 'Computador', 'Centro Comercial Sucupira', 'funcionando'),
(1412, 'Computador', 'Centro Comercial Sucupira', 'funcionando'),
(1413, 'Computador', 'Centro Comercial Sucupira', 'funcionando'),
(1414, 'Computador', 'Fazenda', 'funcionando'),
(1415, 'Computador', 'Fazenda', 'funcionando'),
(1416, 'Computador', 'Fazenda', 'funcionando'),
(1417, 'Computador', 'Fazenda', 'funcionando'),
(1418, 'Computador', 'Fazenda', 'funcionando'),
(1419, 'Computador', 'Palmarejo', 'funcionando'),
(1420, 'Computador', 'Palmarejo', 'funcionando'),
(1421, 'Computador', 'Palmarejo', 'danificado'),
(1422, 'Computador', 'Palmarejo', 'funcionando'),
(1423, 'Computador', 'Palmarejo', 'funcionando'),
(1424, 'Computador', 'Sede', 'funcionando'),
(1425, 'Computador', 'Sede', 'funcionando'),
(1426, 'Computador', 'Sede', 'funcionando'),
(1427, 'Computador', 'Sede', 'funcionando'),
(1428, 'Computador', 'Sede', 'funcionando'),
(1429, 'Computador', 'Sede', 'funcionando'),
(1430, 'Computador', 'Sede', 'funcionando'),
(1431, 'Computador', 'Plato', 'funcionando'),
(1432, 'Computador', 'Plato', 'funcionando'),
(1433, 'Computador', 'Plato', 'funcionando'),
(1434, 'Computador', 'Plato', 'funcionando'),
(1435, 'Computador', 'Plato', 'funcionando'),
(1436, 'Computador', 'Plato', 'funcionando'),
(1437, 'Computador', 'Plato', 'funcionando'),
(1501, 'Impressora', 'Achada S. Filipe', 'funcionando'),
(1502, 'Impressora', 'Achada S. Filipe', 'funcionando'),
(1503, 'Impressora', 'Achada S. Filipe', 'funcionando'),
(1504, 'Impressora', 'Achada S. Filipe', 'funcionando'),
(1505, 'Impressora', 'Achada Sto. António', 'funcionando'),
(1506, 'Impressora', 'Achada Sto. António', 'funcionando'),
(1507, 'Impressora', 'Achada Sto. António', 'funcionando'),
(1508, 'Impressora', 'Achada Sto. António', 'funcionando'),
(1509, 'Impressora', 'Achada Sto. António', 'funcionando'),
(1510, 'Impressora', 'Centro Comercial Sucupira', 'funcionando'),
(1511, 'Impressora', 'Centro Comercial Sucupira', 'funcionando'),
(1512, 'Impressora', 'Centro Comercial Sucupira', 'funcionando'),
(1513, 'Impressora', 'Centro Comercial Sucupira', 'funcionando'),
(1514, 'Impressora', 'Fazenda', 'funcionando'),
(1515, 'Impressora', 'Fazenda', 'funcionando'),
(1516, 'Impressora', 'Fazenda', 'funcionando'),
(1517, 'Impressora', 'Fazenda', 'funcionando'),
(1518, 'Impressora', 'Fazenda', 'funcionando'),
(1519, 'Impressora', 'Palmarejo', 'funcionando'),
(1520, 'Impressora', 'Palmarejo', 'funcionando'),
(1521, 'Impressora', 'Palmarejo', 'funcionando'),
(1522, 'Impressora', 'Palmarejo', 'funcionando'),
(1523, 'Impressora', 'Palmarejo', 'funcionando'),
(1524, 'Impressora', 'Sede', 'funcionando'),
(1525, 'Impressora', 'Sede', 'funcionando'),
(1526, 'Impressora', 'Sede', 'funcionando'),
(1527, 'Impressora', 'Sede', 'funcionando'),
(1528, 'Impressora', 'Sede', 'funcionando'),
(1529, 'Impressora', 'Sede', 'funcionando'),
(1530, 'Impressora', 'Sede', 'funcionando'),
(1531, 'Impressora', 'Plato', 'funcionando'),
(1532, 'Impressora', 'Plato', 'funcionando'),
(1533, 'Impressora', 'Plato', 'funcionando'),
(1534, 'Impressora', 'Plato', 'funcionando'),
(1535, 'Impressora', 'Plato', 'funcionando'),
(1536, 'Impressora', 'Plato', 'funcionando'),
(1537, 'Impressora', 'Plato', 'funcionando'),
(1601, 'router', 'Achada S. Filipe', 'funcionando'),
(1602, 'router', 'Achada Sto. António', 'funcionando'),
(1603, 'router', 'Aeroporto da Praia', 'funcionando'),
(1604, 'router', 'Centro Comercial Sucupira', 'funcionando'),
(1605, 'router', 'Fazenda', 'funcionando'),
(1606, 'router', 'Palmarejo', 'funcionando'),
(1607, 'router', 'Sede', 'funcionando'),
(1608, 'router', 'Plato', 'funcionando'),
(1701, 'switch', 'Achada S. Filipe', 'funcionando'),
(1702, 'switch', 'Achada Sto. António', 'funcionando'),
(1703, 'switch', 'Aeroporto da Praia', 'funcionando'),
(1704, 'switch', 'Centro Comercial Sucupira', 'funcionando'),
(1705, 'switch', 'Fazenda', 'funcionando'),
(1706, 'switch', 'Palmarejo', 'funcionando'),
(1707, 'switch', 'Sede', 'funcionando'),
(1708, 'switch', 'Sede', 'funcionando'),
(1709, 'switch', 'Plato', 'funcionando'),
(1710, 'switch', 'Plato', 'funcionando'),
(1801, 'Mouse', 'Achada S. Filipe', 'funcionando'),
(1802, 'Mouse', 'Achada S. Filipe', 'funcionando'),
(1803, 'Mouse', 'Achada S. Filipe', 'funcionando'),
(1804, 'Mouse', 'Achada S. Filipe', 'funcionando'),
(1805, 'Mouse', 'Achada Sto. António', 'funcionando'),
(1806, 'Mouse', 'Achada Sto. António', 'funcionando'),
(1807, 'Mouse', 'Achada Sto. António', 'funcionando'),
(1808, 'Mouse', 'Achada Sto. António', 'danificado'),
(1809, 'Mouse', 'Achada Sto. António', 'funcionando'),
(1810, 'Mouse', 'Centro Comercial Sucupira', 'funcionando'),
(1811, 'Mouse', 'Centro Comercial Sucupira', 'funcionando'),
(1812, 'Mouse', 'Centro Comercial Sucupira', 'funcionando'),
(1813, 'Mouse', 'Centro Comercial Sucupira', 'funcionando'),
(1814, 'Mouse', 'Fazenda', 'funcionando'),
(1815, 'Mouse', 'Fazenda', 'funcionando'),
(1816, 'Mouse', 'Fazenda', 'funcionando'),
(1817, 'Mouse', 'Fazenda', 'funcionando'),
(1818, 'Mouse', 'Fazenda', 'funcionando'),
(1819, 'Mouse', 'Palmarejo', 'funcionando'),
(1820, 'Mouse', 'Palmarejo', 'funcionando'),
(1821, 'Mouse', 'Palmarejo', 'danificado'),
(1822, 'Mouse', 'Palmarejo', 'funcionando'),
(1823, 'Mouse', 'Palmarejo', 'funcionando'),
(1824, 'Mouse', 'Sede', 'funcionando'),
(1825, 'Mouse', 'Sede', 'funcionando'),
(1826, 'Mouse', 'Sede', 'funcionando'),
(1827, 'Mouse', 'Sede', 'funcionando'),
(1828, 'Mouse', 'Sede', 'funcionando'),
(1829, 'Mouse', 'Sede', 'funcionando'),
(1830, 'Mouse', 'Sede', 'funcionando'),
(1831, 'Mouse', 'Plato', 'funcionando'),
(1832, 'Mouse', 'Plato', 'funcionando'),
(1833, 'Mouse', 'Plato', 'funcionando'),
(1834, 'Mouse', 'Plato', 'funcionando'),
(1835, 'Mouse', 'Plato', 'funcionando'),
(1836, 'Mouse', 'Plato', 'funcionando'),
(1837, 'Mouse', 'Plato', 'funcionando'),
(1900, 'Teclado', 'Achada S. Filipe', 'funcionando'),
(1901, 'Teclado', 'Achada S. Filipe', 'funcionando'),
(1902, 'Teclado', 'Achada S. Filipe', 'funcionando'),
(1903, 'Teclado', 'Achada S. Filipe', 'funcionando'),
(1904, 'Teclado', 'Achada Sto. António', 'funcionando'),
(1905, 'Teclado', 'Achada Sto. António', 'funcionando'),
(1906, 'Teclado', 'Achada Sto. António', 'funcionando'),
(1907, 'Teclado', 'Achada Sto. António', 'danificado'),
(1908, 'Teclado', 'Achada Sto. António', 'funcionando'),
(1909, 'Teclado', 'Centro Comercial Sucupira', 'funcionando'),
(1910, 'Teclado', 'Centro Comercial Sucupira', 'funcionando'),
(1911, 'Teclado', 'Centro Comercial Sucupira', 'funcionando'),
(1912, 'Teclado', 'Centro Comercial Sucupira', 'funcionando'),
(1913, 'Teclado', 'Fazenda', 'funcionando'),
(1914, 'Teclado', 'Fazenda', 'funcionando'),
(1915, 'Teclado', 'Fazenda', 'funcionando'),
(1916, 'Teclado', 'Fazenda', 'funcionando'),
(1917, 'Teclado', 'Fazenda', 'funcionando'),
(1918, 'Teclado', 'Palmarejo', 'funcionando'),
(1919, 'Teclado', 'Palmarejo', 'funcionando'),
(1920, 'Teclado', 'Palmarejo', 'danificado'),
(1921, 'Teclado', 'Palmarejo', 'funcionando'),
(1922, 'Teclado', 'Palmarejo', 'funcionando'),
(1923, 'Teclado', 'Sede', 'funcionando'),
(1924, 'Teclado', 'Sede', 'funcionando'),
(1925, 'Teclado', 'Sede', 'funcionando'),
(1926, 'Teclado', 'Sede', 'funcionando'),
(1927, 'Teclado', 'Sede', 'funcionando'),
(1928, 'Teclado', 'Sede', 'funcionando'),
(1929, 'Teclado', 'Sede', 'funcionando'),
(1930, 'Teclado', 'Plato', 'funcionando'),
(1931, 'Teclado', 'Plato', 'funcionando'),
(1932, 'Teclado', 'Plato', 'funcionando'),
(1933, 'Teclado', 'Plato', 'funcionando'),
(1934, 'Teclado', 'Plato', 'funcionando'),
(1935, 'Teclado', 'Plato', 'funcionando'),
(1936, 'Teclado', 'Plato', 'funcionando'),
(2001, 'Monitor', 'Achada S. Filipe', 'funcionando'),
(2002, 'Monitor', 'Achada S. Filipe', 'funcionando'),
(2003, 'Monitor', 'Achada S. Filipe', 'funcionando'),
(2004, 'Monitor', 'Achada S. Filipe', 'funcionando'),
(2005, 'Monitor', 'Achada Sto. António', 'funcionando'),
(2006, 'Monitor', 'Achada Sto. António', 'funcionando'),
(2007, 'Monitor', 'Achada Sto. António', 'funcionando'),
(2008, 'Monitor', 'Achada Sto. António', 'funcionando'),
(2009, 'Monitor', 'Achada Sto. António', 'funcionando'),
(2010, 'Monitor', 'Centro Comercial Sucupira', 'funcionando'),
(2011, 'Monitor', 'Centro Comercial Sucupira', 'funcionando'),
(2012, 'Monitor', 'Centro Comercial Sucupira', 'funcionando'),
(2013, 'Monitor', 'Centro Comercial Sucupira', 'funcionando'),
(2014, 'Monitor', 'Fazenda', 'funcionando'),
(2015, 'Monitor', 'Fazenda', 'funcionando'),
(2016, 'Monitor', 'Fazenda', 'funcionando'),
(2017, 'Monitor', 'Fazenda', 'funcionando'),
(2018, 'Monitor', 'Fazenda', 'funcionando'),
(2019, 'Monitor', 'Palmarejo', 'funcionando'),
(2020, 'Monitor', 'Palmarejo', 'funcionando'),
(2021, 'Monitor', 'Palmarejo', 'danificado'),
(2022, 'Monitor', 'Palmarejo', 'funcionando'),
(2023, 'Monitor', 'Palmarejo', 'funcionando'),
(2024, 'Monitor', 'Sede', 'funcionando'),
(2025, 'Monitor', 'Sede', 'funcionando'),
(2026, 'Monitor', 'Sede', 'funcionando'),
(2027, 'Monitor', 'Sede', 'funcionando'),
(2028, 'Monitor', 'Sede', 'funcionando'),
(2029, 'Monitor', 'Sede', 'funcionando'),
(2030, 'Monitor', 'Sede', 'funcionando'),
(2031, 'Monitor', 'Plato', 'funcionando'),
(2032, 'Monitor', 'Plato', 'funcionando'),
(2033, 'Monitor', 'Plato', 'funcionando'),
(2034, 'Monitor', 'Plato', 'funcionando'),
(2035, 'Monitor', 'Plato', 'funcionando'),
(2036, 'Monitor', 'Plato', 'funcionando'),
(2037, 'Monitor', 'Plato', 'funcionando'),
(2100, 'Ar-Condicionado', 'Achada S. Filipe', 'funcionando'),
(2101, 'Ar-Condicionado', 'Achada S. Filipe', 'funcionando'),
(2102, 'Ar-Condicionado', 'Achada S. Filipe', 'funcionando'),
(2103, 'Ar-Condicionado', 'Achada S. Filipe', 'funcionando'),
(2104, 'Ar-Condicionado', 'Achada Sto. António', 'funcionando'),
(2105, 'Ar-Condicionado', 'Achada Sto. António', 'funcionando'),
(2106, 'Ar-Condicionado', 'Achada Sto. António', 'funcionando'),
(2107, 'Ar-Condicionado', 'Achada Sto. António', 'danificado'),
(2108, 'Ar-Condicionado', 'Achada Sto. António', 'funcionando'),
(2109, 'Ar-Condicionado', 'Centro Comercial Sucupira', 'funcionando'),
(2110, 'Ar-Condicionado', 'Centro Comercial Sucupira', 'funcionando'),
(2111, 'Ar-Condicionado', 'Centro Comercial Sucupira', 'funcionando'),
(2112, 'Ar-Condicionado', 'Centro Comercial Sucupira', 'funcionando'),
(2113, 'Ar-Condicionado', 'Fazenda', 'funcionando'),
(2114, 'Ar-Condicionado', 'Fazenda', 'funcionando'),
(2115, 'Ar-Condicionado', 'Fazenda', 'funcionando'),
(2116, 'Ar-Condicionado', 'Fazenda', 'funcionando'),
(2117, 'Ar-Condicionado', 'Fazenda', 'funcionando'),
(2118, 'Ar-Condicionado', 'Palmarejo', 'funcionando'),
(2119, 'Ar-Condicionado', 'Palmarejo', 'funcionando'),
(2120, 'Ar-Condicionado', 'Palmarejo', 'danificado'),
(2121, 'Ar-Condicionado', 'Palmarejo', 'funcionando'),
(2122, 'Ar-Condicionado', 'Palmarejo', 'funcionando'),
(2123, 'Ar-Condicionado', 'Sede', 'funcionando'),
(2124, 'Ar-Condicionado', 'Sede', 'funcionando'),
(2125, 'Ar-Condicionado', 'Sede', 'funcionando'),
(2126, 'Ar-Condicionado', 'Sede', 'funcionando'),
(2127, 'Ar-Condicionado', 'Sede', 'funcionando'),
(2128, 'Ar-Condicionado', 'Sede', 'funcionando'),
(2129, 'Ar-Condicionado', 'Sede', 'funcionando'),
(2130, 'Ar-Condicionado', 'Plato', 'funcionando'),
(2131, 'Ar-Condicionado', 'Plato', 'funcionando'),
(2132, 'Ar-Condicionado', 'Plato', 'funcionando'),
(2133, 'Ar-Condicionado', 'Plato', 'funcionando'),
(2134, 'Ar-Condicionado', 'Plato', 'funcionando'),
(2135, 'Ar-Condicionado', 'Plato', 'funcionando'),
(2136, 'Ar-Condicionado', 'Plato', 'funcionando')]

with engine.connect() as connection:
    with connection.begin() as transaction:
        try:
            markers = ','.join('?' * len(values[0]))
            ins = 'INSERT INTO {tablename} VALUES ({markers})'
            ins = ins.format(tablename=equipamentos.name, markers=markers)
            connection.execute(ins, values)
        except:
            transaction.rollback()
            raise
        else:
                transaction.commit()
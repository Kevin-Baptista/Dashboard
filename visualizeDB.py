import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='cio')
mycursor=mydb.cursor()


mycursor.execute("select * from equipamentos")
result = mycursor.fetchall
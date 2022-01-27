import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

mydb=mysql.connector.connect(host=”localhost”,user=”root”,password=”Your_Password”,database=”Database_Name”)
mycursor=mydb.cursor()
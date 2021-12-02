import json
import pandas as pd
from complementos.funciones import*
import csv

fechas = csv.DictReader(open("fechas.csv"))
fechas_final = []

for raw in fechas:
    print(raw["fecha"])
    split_fecha = raw.split(",")
    
    month_final = get_mes(split_fecha)
    print(month_final)




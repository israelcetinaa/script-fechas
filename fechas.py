import json
import pandas as pd
from helpers.meses import(mes)
import csv

fechas = csv.DictReader(open("fechas.csv"))

for raw in fechas:
    print(raw)


from meses import(mes_obj)

def get_mes(fecha):
    month = fecha.split()
    month = month[0]
    for m in mes_obj.mes:
        if month == m[1]:
            month = m[2]
        else:
            pass
    return month

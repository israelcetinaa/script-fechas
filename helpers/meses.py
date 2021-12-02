class Meses:
    def __init__(self, mes):
        self.mes = mes

meses = [
    ("Enero"     , "Jan", 1),
    ("Febrero"   , "Feb", 2),
    ("Marzo"     , "Mar", 3),
    ("Abril"     , "Apr", 4),
    ("Mayo"      , "May", 5),
    ("Junio"     , "Jun", 6),
    ("julio"     , "Jul", 7),
    ("Agosto"    , "Aug", 8),
    ("Septiembre", "Sep", 9),
    ("Octubre"   , "Oct", 10),
    ("Noviembre" , "Nov", 11),
    ("Diciembre" , "Dec", 12)
]

mes = Meses(meses)
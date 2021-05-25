# trabajar con fechas
from datetime import datetime 

hoy = datetime.today()
print(hoy)
print("el dia es {}".format(hoy.day))
print("el mes es {}".format(hoy.month))
print("el año es {}".format(hoy.year))
ahora = datetime.now()
print(ahora)
formato = ahora.strftime('Dia: %d, Mes: %m, Año: %Y, Hora: %H, Min: %M, Seg: %S')
print(formato)
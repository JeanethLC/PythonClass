#Graba las lineas de la 15 a la 20 en otro archivo de texto
import unittest

doc = open("Licc.txt", "r")
doc2 = open("Nuevo.txt", "w")
ini = 15
fin = 20
j = 0
for linea in doc:
    j = j + 1
    if j >= ini and j < fin:
        doc2.write(linea)
doc.close()
doc2.close()

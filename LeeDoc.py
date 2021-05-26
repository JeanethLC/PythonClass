import unittest

doc = open("Licc.txt", "r")
j = 0
for linea in doc:
    if j < 10:
        print(linea)
        j = j + 1
doc.close()
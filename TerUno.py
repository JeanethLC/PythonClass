import unittest

numero = 0
suma = 0
while numero <= 7:
    suma = suma + numero
    numero = numero + 1
print ('la suma total es ' + str(suma))

class TestResult(unittest.TestCase):
    def test_result(self):
        self.assertTrue(suma)

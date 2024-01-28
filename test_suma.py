import unittest
from suma import sumar, restar, multiplicar, dividir

class TestSumar(unittest.TestCase):
  
  def test_sumar(self):
    self.assertEqual(sumar(3, 2), 5)
    self.assertEqual(sumar(-1, 1), 0)
    self.assertEqual(sumar(-1, -1), -2)


class TestRestar(unittest.TestCase):

  def test_restar(self):
    self.assertEqual(restar(3, 2), 1)
    self.assertEqual(restar(5, 2), 3)
    self.assertEqual(restar(0, 2), -2)
    self.assertEqual(restar(40, 28), 12)

class TestMultiplicar(unittest.TestCase):

  def test_multiplicar(self):
    self.assertEqual(multiplicar(3, 2), 6)
    self.assertEqual(multiplicar(20, 2), 40)
    self.assertEqual(multiplicar(5, 10), 50)
    self.assertEqual(multiplicar(40, 28), 1120)


class TestDividir(unittest.TestCase):

  def test_dividir(self):
    self.assertEqual(dividir(6, 2), 3)
    self.assertEqual(dividir(20, 0), {"error: no se puede dividir entre 0"})
    self.assertEqual(dividir(20, 10), 2)
    self.assertEqual(dividir(10, 2), 5)



if __name__ == '__main__':
  unittest.main()
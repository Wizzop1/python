import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result=calc.add(10,5)
        self.assertEquals(result,15)
        self.assertEqual(calc.add(1,5),6)
    def test_substract(self):
        result=calc.subtract(10,5)
        self.assertEquals(result,5)
        self.assertEqual(calc.subtract(3,3),0)
    def test_multiply(self):
        result=calc.multiply(5,5)
        self.assertEquals(result,25)
        self.assertEqual(calc.multiply(4,3),12)
    def test_divide(self):
        self.assertEquals(calc.divide(5,5),1)
        with self.assertRaises(ValueError):
            calc.divide(10,0)

if __name__== '__main__':
    unittest.main()

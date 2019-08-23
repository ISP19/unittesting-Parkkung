import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):


    def test_init(self):
        """test for fraction construction
        """
        f = Fraction(5)
        self.assertEquals(1,f.denominator)
        f = Fraction(5, -3)
        self.assertEqual(-5, f.numerator)
        f = Fraction(-8, -3)
        self.assertEqual(8, f.numerator)
        f = Fraction(0, 2)
        self.assertEqual(0, f.numerator)
        f = Fraction(5, 9)
        self.assertEqual(9, f.denominator)
        f = Fraction(1, -6)
        self.assertEqual(6, f.denominator)
        f = Fraction(1, 3)
        self.assertEqual(3, f.denominator)
        f = Fraction(0, 4)
        self.assertEqual(0, f.numerator)

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        # 31 / 35 = 3 / 5 + 2 / 7
        self.assertEqual(Fraction(30, 35), Fraction(3, 5) + Fraction(2, 7))

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        #TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0



if __name__ == '__main__':
    unittest.main(fraction_test)
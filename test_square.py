import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    def test_zero(self):
        area_res = area(0)
        self.assertEqual(area_res, 0)

        per_res = perimeter(0)
        self.assertEqual(per_res, 0)
    
    def test_big_numbers(self):
        area_res = area(12345678910111213)
        self.assertEqual(area_res, 152415787751564788077248028331369)

        per_res = perimeter(12345678910111213)
        self.assertEqual(per_res, 49382715640444852)

    def test_one(self):
        area_res = area(1)
        self.assertEqual(area_res, 1)

        per_res = perimeter(1)
        self.assertEqual(per_res, 4)
    
    def test_float(self):
        area_res = area(10.5)
        self.assertEqual(area_res, 110.25)

        per_res = perimeter(10.5)
        self.assertEqual(per_res, 42)
    
    def test_big_numbers_float(self):
        area_res = area(12345678910111213.123)
        self.assertEqual(area_res, 1.5241578775156482e+32)

        per_res = perimeter(12345678910111213.123)
        self.assertEqual(per_res, 4.9382715640444856e+16)
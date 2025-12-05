import unittest
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_zero(self):
        area_res = area(0)
        self.assertEqual(area_res, 0)

        per_res = perimeter(0)
        self.assertEqual(per_res, 0)
    
    def test_big_numbers(self):
        area_res = area(12345678910111213)
        self.assertEqual(area_res, 4.78828319091417e+32)

        per_res = perimeter(12345678910111213)
        self.assertEqual(per_res, 7.757018833516765e+16)

    def test_one(self):
        area_res = area(1)
        self.assertEqual(area_res, 3.141592653589793)

        per_res = perimeter(1)
        self.assertEqual(per_res, 6.283185307179586)
    
    def test_float(self):
        area_res = area(10.5)
        self.assertEqual(area_res, 346.36059005827474)

        per_res = perimeter(10.5)
        self.assertEqual(per_res, 65.97344572538566)
    
    def test_big_numbers_float(self):
        area_res = area(12345678910111213.123)
        self.assertEqual(area_res, 4.788283190914171e+32)

        per_res = perimeter(12345678910111213.123)
        self.assertEqual(per_res, 7.757018833516766e+16)
    
    def test_negative(self):
        area_res = area(-10)
        self.assertEqual(area_res, None)

        per_res = perimeter(-10)
        self.assertEqual(per_res, None)
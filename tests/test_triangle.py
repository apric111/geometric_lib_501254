import unittest
import math
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area_res1 = area(10, 0)
        area_res2 = area(0, 10)
        self.assertEqual(area_res1, 0)
        self.assertEqual(area_res2, 0)
        self.assertEqual(area_res1, area_res2)

        per_res = perimeter(5, 5, 0)
        self.assertEqual(per_res, 10)
    
    def test_big_numbers(self):
        area_res1 = area(12345678910111213, 987654321)
        area_res2 = area(987654321, 12345678910111213)
        self.assertEqual(area_res1, 6.096631560624955e+24)
        self.assertEqual(area_res2, 6.096631560624955e+24)
        self.assertEqual(area_res1, area_res2)

        per_res = perimeter(5000, 5000, 7000)
        self.assertEqual(per_res, 17000)

    def test_one(self):
        area_res1 = area(10, 1)
        area_res2 = area(1, 10)
        self.assertEqual(area_res1, 5)
        self.assertEqual(area_res2, 5)
        self.assertEqual(area_res1, area_res2)

        per_res = perimeter(1, 3, math.sqrt(10))
        self.assertEqual(per_res, 7.16227766016838)
    
    def test_zero_mul_float(self):
        area_res1 = area(10.5, 0)
        area_res2 = area(0, 10.5)
        self.assertEqual(area_res1, 0)
        self.assertEqual(area_res2, 0)
        self.assertEqual(area_res1, area_res2)

        per_res = perimeter(5.25, 5.25, 7.3)
        self.assertEqual(per_res, 17.8)
    
    def test_big_numbers_float(self):
        area_res1 = area(12345678910111213.123, 987654321.321)
        area_res2 = area(987654321.321, 12345678910111213.123)
        self.assertEqual(area_res1, 6.096631562606437e+24)
        self.assertEqual(area_res2, 6.096631562606437e+24)
        self.assertEqual(area_res1, area_res2)

        per_res = perimeter(12345.67, 98765.43, 111111.11)
        self.assertEqual(per_res, 222222.21)

    def test_one_float(self):
        area_res1 = area(10.5, 1)
        area_res2 = area(1, 10.5)
        self.assertEqual(area_res1, 5.25)
        self.assertEqual(area_res2, 5.25)
        self.assertEqual(area_res1, area_res2)

        per_res = perimeter(1, 3.5, math.sqrt(13.25))
        self.assertEqual(per_res, 8.140054944640259)
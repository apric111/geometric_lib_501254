import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area_res1 = area(10, 0)
        area_res2 = area(0, 10)
        self.assertEqual(area_res1, 0)
        self.assertEqual(area_res2, 0)
        self.assertEqual(area_res1, area_res2)

        per_res1 = perimeter(10, 0)
        per_res2 = perimeter(0, 10)
        self.assertEqual(per_res1, 20)
        self.assertEqual(per_res2, 20)
        self.assertEqual(per_res1, per_res2)
    
    def test_square_mul(self):
        area_res = area(10, 10)
        self.assertEqual(area_res, 100)

        per_res = perimeter(10, 10)
        self.assertEqual(per_res, 40)
    
    def test_big_numbers(self):
        area_res1 = area(12345678910111213, 987654321)
        area_res2 = area(987654321, 12345678910111213)
        self.assertEqual(area_res1, 12193263121249910110001373)
        self.assertEqual(area_res2, 12193263121249910110001373)
        self.assertEqual(area_res1, area_res2)

        per_res1 = perimeter(12345678910111213, 987654321)
        per_res2 = perimeter(987654321, 12345678910111213)
        self.assertEqual(per_res1, 24691359795531068)
        self.assertEqual(per_res2, 24691359795531068)
        self.assertEqual(per_res1, per_res2)

    def test_one_mul(self):
        area_res1 = area(10, 1)
        area_res2 = area(1, 10)
        self.assertEqual(area_res1, 10)
        self.assertEqual(area_res2, 10)
        self.assertEqual(area_res1, area_res2)

        per_res1 = perimeter(10, 1)
        per_res2 = perimeter(1, 10)
        self.assertEqual(per_res1, 22)
        self.assertEqual(per_res2, 22)
        self.assertEqual(per_res1, per_res2)
    
    def test_zero_mul_float(self):
        area_res1 = area(10.5, 0)
        area_res2 = area(0, 10.5)
        self.assertEqual(area_res1, 0)
        self.assertEqual(area_res2, 0)
        self.assertEqual(area_res1, area_res2)

        per_res1 = perimeter(10.5, 0)
        per_res2 = perimeter(0, 10.5)
        self.assertEqual(per_res1, 21)
        self.assertEqual(per_res2, 21)
        self.assertEqual(per_res1, per_res2)
    
    def test_square_mul_float(self):
        area_res = area(10.5, 10.5)
        self.assertEqual(area_res, 110.25)

        per_res = perimeter(10.5, 10.5)
        self.assertEqual(per_res, 42)
    
    def test_big_numbers_float(self):
        area_res1 = area(12345678910111213.123, 987654321.321)
        area_res2 = area(987654321.321, 12345678910111213.123)
        self.assertEqual(area_res1, 1.2193263125212874e+25)
        self.assertEqual(area_res2, 1.2193263125212874e+25)
        self.assertEqual(area_res1, area_res2)

        per_res1 = perimeter(12345678910111213.123, 987654321.321)
        per_res2 = perimeter(987654321.321, 12345678910111213.123)
        self.assertEqual(per_res1, 2.469135979553107e+16)
        self.assertEqual(per_res2, 2.469135979553107e+16)
        self.assertEqual(per_res1, per_res2)

    def test_one_mul_float(self):
        area_res1 = area(10.5, 1)
        area_res2 = area(1, 10.5)
        self.assertEqual(area_res1, 10.5)
        self.assertEqual(area_res2, 10.5)
        self.assertEqual(area_res1, area_res2)

        per_res1 = perimeter(10.5, 1)
        per_res2 = perimeter(1, 10.5)
        self.assertEqual(per_res1, 23)
        self.assertEqual(per_res2, 23)
        self.assertEqual(per_res1, per_res2)
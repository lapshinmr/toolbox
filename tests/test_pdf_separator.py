import unittest
from separate import *


class TestFunctions(unittest.TestCase):
    def test_make_range(self):
        case = [
            ('', ()),
            ('1', (0, 1)),
            ('11-14', (10, 14)),
            ('11--14', [(10, 11), (11, 12), (12, 13), (13, 14)]),
            ('11--14(2)', [(10, 12), (12, 14)]),
            ('11--16(2)', [(10, 12), (12, 14), (14, 16)]),
        ]
        for from_, to_ in case:
            self.assertEqual(make_range(from_), to_)

    def test_make_ranges(self):
        case = [
            (['1', '2', '2-4'], [(0, 1), (1, 2), (1, 4)]),
            (['1', '2', '3--5'], [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]),
            (['8--141(2)', '142', '143--192(2)', '193', '194', '195--206(2)'], [(10, 12), (12, 14), (14, 16)]),
        ]
        for from_, to_ in case:
            self.assertEqual(make_ranges(from_), to_)

import unittest

import code7 as c


class Test(unittest.TestCase):
    def test_task1_mean(self):
        values = [1, 2, 2, 3, 2, 1, 4, 2, 3, 1, 0]
        self.assertAlmostEqual(1.90909, c.mean(values), 5)

    def test_task1_mode(self):
        values = [1, 2, 2, 3, 2, 1, 4, 2, 3, 1, 0]
        self.assertEqual(2, c.mode(values))

    def test_task1_median(self):
        values = [1, 2, 2, 3, 2, 1, 4, 2, 3, 1, 0]
        self.assertEqual(2, c.median(values))

    def test_task1_standard_deviation(self):
        values = [1, 2, 2, 3, 2, 1, 4, 2, 3, 1, 0]
        self.assertAlmostEqual(1.17355, c.standard_deviation(values), 5)

    def test_task1_dispersion(self):
        values = [1, 2, 2, 3, 2, 1, 4, 2, 3, 1, 0]
        self.assertAlmostEqual(1.083306, c.dispersion(values), 5)


if __name__ == "__main__":
    unittest.main()

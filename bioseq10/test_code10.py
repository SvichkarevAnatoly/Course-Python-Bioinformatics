import unittest

import code10 as c


class Test(unittest.TestCase):
    def test_task1_multiple_linear_regression(self):
        y = [12.2, 7.6, 10.4, 9.9, 15.7, 14.0, 12.7, 10.5, 15.1, 10.6]
        x1 = [4795, 6962, 6571, 4249, 9540, 3488, 4888, 6237, 2997, 2990]
        x2 = [69, 82, 87, 92, 23, 31, 55, 81, 65, 98]

        intercept, coeff_x1, coeff_x2 = c.mlr(y, x1, x2)

        self.assertAlmostEqual(19.857755, intercept, 5)
        self.assertAlmostEqual(-0.000359, coeff_x1, 5)
        self.assertAlmostEqual(-0.089194, coeff_x2, 5)


if __name__ == "__main__":
    unittest.main()

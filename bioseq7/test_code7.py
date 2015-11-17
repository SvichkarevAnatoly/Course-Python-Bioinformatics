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

    def test_task2(self):
        values = [1.752, 1.818, 1.597, 1.697, 1.644, 1.593, 1.878, 1.648,
                  1.819, 1.794, 1.745, 1.827]
        mean, interval = c.confidence_interval(values, 0.95, False)
        self.assertAlmostEqual(1.734, mean, 3)
        self.assertAlmostEqual(0.0615, interval, 4)

    def test_task3(self):
        import numpy

        numpy.random.seed(0)
        xVals = numpy.random.normal(0.0, 1.0, 100)
        yVals = 2.0 + -0.7 * xVals + numpy.random.normal(0.0, 0.2, 100)

        grad, yInt = c.line_regression_numpy(xVals, yVals)

        self.assertAlmostEqual(-0.677, grad, 3)
        self.assertAlmostEqual(2.015, yInt, 3)

    def test_task4(self):
        import numpy

        numpy.random.seed(0)
        xVals = numpy.random.normal(0.0, 1.0, 100)
        yVals = 2.0 + -0.7 * xVals + numpy.random.normal(0.0, 0.2, 100)

        grad, yInt, corrCoeff, pValue, stdErr = c.line_regression_linregress(
            xVals, yVals)

        self.assertAlmostEqual(-0.677, grad, 3)
        self.assertAlmostEqual(2.015, yInt, 3)
        self.assertAlmostEqual(-0.957, corrCoeff, 3)
        self.assertAlmostEqual(0, pValue, 3)
        self.assertAlmostEqual(0.0206, stdErr, 3)


if __name__ == "__main__":
    unittest.main()

import unittest

import code8 as c

sample = [1, 2, 2, 3, 2, 1, 4, 2, 3, 1, 0]


class Test(unittest.TestCase):
    def test_task1(self):
        samples1 = [1.752, 1.818, 1.597, 1.697, 1.644, 1.593]
        samples2 = [1.878, 1.648, 1.819, 1.794, 1.745, 1.827]

        t, p_value = c.t_test(samples1, samples2, same_variance=True)
        self.assertAlmostEqual(-2.072, t, 3)
        self.assertAlmostEqual(0.0650, p_value, 4)

        t, p_value = c.t_test(samples1, samples2)
        self.assertAlmostEqual(-2.072, t, 3)
        self.assertAlmostEqual(0.0654, p_value, 4)

    def test_task2_mean(self):
        self.assertAlmostEqual(1.909091, c.mean(sample), 6)

    def test_task2_mode(self):
        self.assertEqual(2, c.mode(sample))

    def test_task2_median(self):
        self.assertEqual(2, c.median(sample))

    def test_task2_dispersion(self):
        self.assertAlmostEqual(1.290909, c.dispersion(sample), 6)

    def test_task2_standard_deviation(self):
        self.assertAlmostEqual(1.1361818, c.standard_deviation(sample), 6)

    def test_task3_confidence_interval(self):
        sample3 = [1.752, 1.818, 1.597, 1.697,
                   1.644, 1.593, 1.878, 1.648,
                   1.819, 1.794, 1.745, 1.827]
        mean, interval = c.confidence_interval(sample3)
        self.assertAlmostEqual(1.734, mean, 3)
        self.assertAlmostEqual(0.0615, interval, 4)


if __name__ == "__main__":
    unittest.main()

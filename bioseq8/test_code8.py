import unittest

import code8 as c


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



if __name__ == "__main__":
    unittest.main()

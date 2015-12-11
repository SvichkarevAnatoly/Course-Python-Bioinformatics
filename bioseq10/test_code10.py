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

    def test_task2_generate_norm(self):
        # reproduce the results
        import rpy2.robjects as r
        r.r('''set.seed(0)''')

        observation_number = 2
        norm_array = c.norm(observation_number)
        self.assertEqual(2, len(norm_array))
        self.assertAlmostEqual(1.26295428, norm_array[0])
        self.assertAlmostEqual(-0.32623336, norm_array[1])

    def test_task2_generate_gamma(self):
        # reproduce the results
        import rpy2.robjects as r
        r.r('''set.seed(0)''')

        observation_number = 2
        gamma_array = c.gamma(observation_number)
        self.assertEqual(2, len(gamma_array))
        self.assertAlmostEqual(1.79180692, gamma_array[0])
        self.assertAlmostEqual(0.29592522, gamma_array[1])

    def test_task2_generate_lnorm(self):
        # reproduce the results
        import rpy2.robjects as r
        r.r('''set.seed(0)''')

        observation_number = 2
        lnorm_array = c.lnorm(observation_number)
        self.assertEqual(2, len(lnorm_array))
        self.assertAlmostEqual(3.53585198, lnorm_array[0])
        self.assertAlmostEqual(0.72163676, lnorm_array[1])

    def test_task3_param_norm(self):
        # reproduce the results
        import rpy2.robjects as r
        r.r('''set.seed(0)''')

        observation_number = 100
        norm_array = c.norm(observation_number)
        mean, sd = c.param_norm(norm_array)
        self.assertAlmostEqual(0.02266844, mean)
        self.assertAlmostEqual(0.88265019, sd)

    def test_task3_param_gamma(self):
        # reproduce the results
        import rpy2.robjects as r
        r.r('''set.seed(0)''')

        observation_number = 100
        gamma_array = c.gamma(observation_number)
        shape, scale = c.param_gamma(gamma_array)
        self.assertAlmostEqual(0.87414224, shape)
        self.assertAlmostEqual(0.87710012, scale)

    def test_task3_param_lnorm(self):
        # reproduce the results
        import rpy2.robjects as r
        r.r('''set.seed(0)''')

        observation_number = 100
        lnorm_array = c.lnorm(observation_number)
        meanlog, sdlog = c.param_lnorm(lnorm_array)
        self.assertAlmostEqual(-0.12957849, meanlog)
        self.assertAlmostEqual(0.74877788, sdlog)


if __name__ == "__main__":
    unittest.main()

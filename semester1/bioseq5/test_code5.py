from random import Random
import unittest

import code5 as c


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.small_training_set = [
            ('ADTLL', 'E'),
            ('DTLLI', 'E'),
            ('TLLIL', 'E'),
            ('LLILG', 'E'),
            ('LILGD', 'E'),
            ('ILGDS', 'E'),
            ('LGDSL', 'C'),
            ('GDSLS', 'H'),
            ('DSLSA', 'H'),
            ('SLSAG', 'H'),
            ('LSAGY', 'H'),
            ('SAGYR', 'C'),
            ('AGYRM', 'C'),
            ('GYRMS', 'C'),
            ('YRMSA', 'C'),
            ('RMSAS', 'C')
        ]

    def test_predict_on_small_training_set_task1(self):
        rand = Random(0)

        nn = c.NeuralNet(rand)
        nn.train(self.small_training_set)

        testSeq = 'DLLSA'
        predictedClass = nn.predict(testSeq)
        self.assertEqual('H', predictedClass)

    def test_use_logistic_function_task3(self):
        rand = Random(0)

        nn = c.NeuralNet(rand, "logistic")
        nn.train(self.small_training_set)

        testSeq = 'DLLSA'
        predictedClass = nn.predict(testSeq)
        # not determined
        self.assertEqual('H', predictedClass)


if __name__ == "__main__":
    unittest.main()

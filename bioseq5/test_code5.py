import random
import unittest

import code5 as c


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seqSecStrucData = [
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

    def test_simple_alignment(self):
        nn = c.NeuralNet()
        nn.train(self.seqSecStrucData)

        testSeq = 'DLLSA'
        predictedClass = nn.predict(testSeq)
        self.assertEqual('H', predictedClass)


if __name__ == "__main__":
    # to get same result of several launches
    random.seed(0)
    unittest.main()

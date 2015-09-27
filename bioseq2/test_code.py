import unittest

import code as c


class Test(unittest.TestCase):
    def test_identify(self):
        seq1 = 'ALIGNMENTS'
        seq2 = 'ALIGDVENTS'
        abs_matching = c.identify(seq1, seq2)
        self.assertEqual(8, abs_matching)


if __name__ == "__main__":
    unittest.main()


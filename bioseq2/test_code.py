import unittest

import code as c


class Test(unittest.TestCase):
    def test_simple_identify(self):
        seq1 = 'ALIGNMENTS'
        seq2 = 'ALIGDVENTS'

        abs_matching, len_alignment, percent, alignment = c.identify(seq1, seq2)

        self.assertEqual(8, abs_matching)
        self.assertEqual(len(seq1), len_alignment)
        self.assertAlmostEqual(80.0, percent, 1)
        self.assertEqual("****  ****", alignment)

    def test_full_identify(self):
        pass

if __name__ == "__main__":
    unittest.main()

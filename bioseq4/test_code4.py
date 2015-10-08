import unittest

import alingment as a
import code4 as c


class Test(unittest.TestCase):
    def test_simple_alignment(self):
        v = "PLEASANTLY"
        w = "MEANLY"
        self.assertEqual(15, a.alignment_score(v, w))
        expected_alignment = "PLEASANTLY\n---MEAN-LY"
        self.assertEqual(expected_alignment, a.alignment(v, w))

    def test_alignment_two_first_from_seqs(self):
        v = c.seqs[0]
        w = c.seqs[1]
        self.assertEqual(157, a.alignment_score(v, w))
        expected_alignment = "QPVHPFSRPAPVVIILIILCVMAGVIGTILLISYGIRLLIK\n" \
                             "QLVHRFTVPAPVVIILIILCVMAGIIGTILLISYTIRRLIK"
        self.assertEqual(expected_alignment, a.alignment(v, w))

    def test_alignment_different_length_seqs(self):
        v = c.seqs[0]
        w = c.seqs[2]
        self.assertEqual(50, a.alignment_score(v, w))
        expected_alignment = "QPVHPFSRPAPVVIILIILCVMAGVIGTILLISYGIR-LL------IK------\n" \
                             "QLAHHFSEPE-IT--LIIFGVMAGVIGTILLISYGIRRLIKKSPSDVKPLPSPD"
        self.assertEqual(expected_alignment, a.alignment(v, w))


if __name__ == "__main__":
    unittest.main()

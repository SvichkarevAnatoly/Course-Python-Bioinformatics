import unittest

import alingment as a
import code4 as c


class Test(unittest.TestCase):
    seqs = [
        'QPVHPFSRPAPVVIILIILCVMAGVIGTILLISYGIRLLIK',
        'QLVHRFTVPAPVVIILIILCVMAGIIGTILLISYTIRRLIK',
        'QLAHHFSEPEITLIIFGVMAGVIGTILLISYGIRRLIKKSPSDVKPLPSPD',
        'QLVHEFSELVIALIIFGVMAGVIGTILFISYGSRRLIKKSESDVQPLPPPD',
        'MLEHEFSAPVAILIILGVMAGIIGIILLISYSIGQIIKKRSVDIQPPEDED',
        'PIQHDFPALVMILIILGVMAGIIGTILLISYCISRMTKKSSVDIQSPEGGD',
        'QLVHIFSEPVIIGIIYAVMLGIIITILSIAFCIGQLTKKSSLPAQVASPED',
        'LAHDFSQPVITVIILGVMAGIIGIILLLAYVSRRLRKRPPADVP',
        'SYHQDFSHAEITGIIFAVMAGLLLIIFLIAYLIRRMIKKPLPVPKPQDSPD'
    ]

    def test_simple_alignment(self):
        v = "PLEASANTLY"
        w = "MEANLY"
        self.assertEqual(15, a.alignment_score(v, w))
        expected_alignment = "PLEASANTLY\n---MEAN-LY"
        self.assertEqual(expected_alignment, a.alignment(v, w))

    def test_alignment_two_first_from_seqs(self):
        v = self.seqs[0]
        w = self.seqs[1]
        self.assertEqual(157, a.alignment_score(v, w))
        expected_alignment = "QPVHPFSRPAPVVIILIILCVMAGVIGTILLISYGIRLLIK\n" \
                             "QLVHRFTVPAPVVIILIILCVMAGIIGTILLISYTIRRLIK"
        self.assertEqual(expected_alignment, a.alignment(v, w))


if __name__ == "__main__":
    unittest.main()

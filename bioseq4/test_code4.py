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

    def test_simple_alignment_score(self):
        v = "PLEASANTLY"
        w = "MEANLY"
        self.assertEqual(15, a.alignment_score(v, w))
        expected_alignment = "PLEASANTLY\n---MEAN-LY"
        self.assertEqual(expected_alignment, a.alignment(v, w))

    def test_alignment_score_from_seqs(self):
        pass

if __name__ == "__main__":
    unittest.main()
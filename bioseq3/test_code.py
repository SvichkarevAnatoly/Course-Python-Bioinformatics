import unittest

import code as c


class Test(unittest.TestCase):
    seqs = [
        "SRPAPVVLIILCVMAGVIGTILLISYGIRLLIK",
        "TVPAPVVIILIILCVMAGIIGTILLLIISYTIRRLIK",
        "HHFSEPEITLIIFGVMAGVIGTILLLIISYGIRLIK",
        "HFSELVIALIIFGVMAGVIGTILFISYGSRLIK"
    ]

    def test_simple_consensus(self):
        seqs = ["AC", "AP"]
        consensus_str = c.consensus(seqs)
        self.assertEqual("AP", consensus_str)

    def test_consensus(self):
        consensus_str = c.consensus(self.seqs)
        expected_consensus_str = "HXPAPVVIIIIIXXVMAGIIGTILLLIISYLIKRIIK"
        self.assertEqual(expected_consensus_str, consensus_str)

if __name__ == "__main__":
    unittest.main()

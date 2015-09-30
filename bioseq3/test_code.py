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

    def test_simple_profile(self):
        seqs = ["AC", "AP"]
        prof = c.profile(seqs)
        expected_profile = [{'A': 2}, {'C': 1, 'P': 1}]
        self.assertEqual(expected_profile, prof)

    def test_profile(self):
        prof = c.profile(self.seqs)
        expected_profile = [
            {'H': 2, 'S': 1, 'T': 1}, {'H': 1, 'F': 1, 'R': 1, 'V': 1}, {'P': 2, 'S': 1, 'F': 1},
            {'A': 2, 'S': 1, 'E': 1}, {'P': 2, 'E': 1, 'L': 1}, {'P': 1, 'V': 3}, {'I': 1, 'E': 1, 'V': 2},
            {'I': 2, 'A': 1, 'L': 1}, {'I': 2, 'T': 1, 'L': 1}, {'I': 2, 'L': 2}, {'I': 3, 'L': 1},
            {'I': 2, 'C': 1, 'F': 1}, {'F': 1, 'L': 1, 'G': 1, 'V': 1}, {'C': 1, 'M': 1, 'G': 1, 'V': 1},
            {'A': 1, 'M': 1, 'V': 2}, {'A': 1, 'M': 2, 'G': 1}, {'A': 2, 'G': 1, 'V': 1}, {'I': 1, 'G': 2, 'V': 1},
            {'I': 2, 'G': 1, 'V': 1}, {'I': 2, 'T': 1, 'G': 1}, {'I': 1, 'T': 1, 'G': 2}, {'I': 1, 'L': 1, 'T': 2},
            {'I': 2, 'L': 2}, {'I': 1, 'L': 2, 'F': 1}, {'I': 1, 'S': 1, 'L': 2}, {'Y': 1, 'S': 1, 'L': 2},
            {'I': 2, 'Y': 1, 'G': 1}, {'I': 3, 'G': 1}, {'S': 3, 'R': 1}, {'Y': 2, 'R': 1, 'L': 1},
            {'L': 2, 'G': 1, 'T': 1}, {'I': 4}, {'K': 2, 'R': 2}, {'R': 1, 'L': 1}, {'I': 1, 'L': 1}, {'I': 1, 'K': 1},
            {'K': 1}
        ]
        self.assertEqual(expected_profile, prof)


if __name__ == "__main__":
    unittest.main()

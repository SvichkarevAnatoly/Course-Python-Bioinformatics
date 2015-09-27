import unittest

import code as c


class Test(unittest.TestCase):
    def check_identify(self, expected, real):
        self.assertEqual(expected[0], real[0])
        self.assertEqual(expected[1], real[1])
        self.assertAlmostEqual(expected[2], real[2], 1)
        self.assertEqual(expected[3], real[3])

    def test_identify(self):
        seqs = [
            "ALIGNMENTS",
            "ALIGDVENTS",
            "ALIGDPVENTS",
            "ALIGN-MENTS"
        ]

        expected_identities = [
            (8, 10, 80.0, "****  ****"),
            (4, 10, 40.0, "****      "),
            (5, 10, 50.0, "*****     "),
            (5, 10, 50.0, "*****     "),
            (4, 10, 40.0, "****      "),
            (8, 11, 72.7, "****   ****")
        ]

        import itertools
        i = 0
        for seq_i, seq_j in list(itertools.combinations(seqs, 2)):
            identity = c.identify(seq_i, seq_j)
            self.check_identify(expected_identities[i], identity)
            i += 1

    def test_similarity_dna(self):
        seq1 = 'AGCATCGCTCT'
        seq2 = 'AGCATCGTTTT'
        similarity = c.similarity_dna(seq1, seq2)
        self.assertEqual(3, similarity)


if __name__ == "__main__":
    unittest.main()

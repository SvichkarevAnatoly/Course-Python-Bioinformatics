import unittest

import code as c


class Test(unittest.TestCase):
    def test_dna_to_rna(self):
        rnaSeq = c.dna_to_rna(c.dnaSeq)
        expected_rnaSeq = 'AUGGUGCAUCUGACUCCUGAGGAGAAGUCUGCCGUUACUGCCCUGUGGGGCAAGGUG'
        self.assertEqual(expected_rnaSeq, rnaSeq)


if __name__ == "__main__":
    unittest.main()

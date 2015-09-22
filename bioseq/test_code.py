import unittest

import code as c


class Test(unittest.TestCase):
    def test_dna_to_rna(self):
        rna_seq = c.dna_to_rna(c.dnaSeq)
        expected_rna_seq = 'AUGGUGCAUCUGACUCCUGAGGAGAAGUCUGCCGUUACUGCCCUGUGGGGCAAGGUG'
        self.assertEqual(expected_rna_seq, rna_seq)

    def test_protein_translation(self):
        protein_seq = c.protein_translation(c.dnaSeq)
        expected_rna_seq = ['Met', 'Val', 'His', 'Leu', 'Thr', 'Pro',
                            'Glu', 'Glu', 'Lys', 'Ser', 'Ala', 'Val',
                            'Thr', 'Ala', 'Leu', 'Trp', 'Gly', 'Lys',
                            'Val']
        self.assertEqual(expected_rna_seq, protein_seq)


if __name__ == "__main__":
    unittest.main()

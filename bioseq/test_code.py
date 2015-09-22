import unittest

import code as c


class Test(unittest.TestCase):
    def test_dna_to_rna(self):
        rna_seq = c.dna_to_rna(c.dna_seq)
        expected_rna_seq = 'AUGGUGCAUCUGACUCCUGAGGAGAAGUCUGCCGUUACUGCCCUGUGGGGCAAGGUG'
        self.assertEqual(expected_rna_seq, rna_seq)

    def test_protein_translation(self):
        protein_seq = c.protein_translation(c.dna_seq)
        expected_rna_seq = ['Met', 'Val', 'His', 'Leu', 'Thr', 'Pro',
                            'Glu', 'Glu', 'Lys', 'Ser', 'Ala', 'Val',
                            'Thr', 'Ala', 'Leu', 'Trp', 'Gly', 'Lys',
                            'Val']
        self.assertEqual(expected_rna_seq, protein_seq)

    def test_estimate_protein_mass(self):
        protein_mass = c.estimate_mol_mass(c.protein_seq)
        expected_protein_mass = 5370.18
        self.assertAlmostEqual(expected_protein_mass, protein_mass, 2)

    def test_estimate_dna_mass(self):
        dna_mass = c.estimate_mol_mass(c.dna_seq, 'DNA')
        expected_dna_mass = 17852.32
        self.assertAlmostEqual(expected_dna_mass, dna_mass, 2)

    def test_estimate_rna_mass(self):
        rna_seq = c.dna_to_rna(c.dna_seq)
        rna_mass = c.estimate_mol_mass(rna_seq, 'RNA')
        expected_rna_mass = 18411.90
        self.assertAlmostEqual(expected_rna_mass, rna_mass, 2)


if __name__ == "__main__":
    unittest.main()

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

    def test_simple_find_subseq(self):
        seq = 'AGCTCGCTCGCTGCGTATAAAATCGCATCGCGCGCAGC'
        position1 = seq.find('TATAAA')
        self.assertEqual(15, position1)

        position2 = seq.find('GAGGAG')
        self.assertEqual(-1, position2)

    def test_match_dna_profile(self):
        profile = {
            'A': [61, 16, 352, 3, 354, 268, 360, 222, 155, 56, 83, 82, 82, 68, 77],
            'C': [145, 46, 0, 10, 0, 0, 3, 2, 44, 135, 147, 127, 118, 107, 101],
            'G': [152, 18, 2, 2, 5, 0, 10, 44, 157, 150, 128, 128, 128, 139, 140],
            'T': [31, 309, 35, 374, 30, 121, 6, 121, 33, 48, 31, 52, 61, 75, 71]
        }
        score, position = c.match_dna_profile(c.dna_seq, profile)
        self.assertEqual(1952, score)
        self.assertEqual(20, position)

        best_match_subseq = c.dna_seq[position:position + 15]
        self.assertEqual(best_match_subseq, "GGAGAAGTCTGCCGT")

    def test_calc_gc_content(self):
        dna_seq = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
        gc_results = c.calc_gc_content(dna_seq)
        print gc_results
        expected_gc_results = \
            [0.5, 0.5, 0.6, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
             0.6, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.5, 0.5,
             0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6,
             0.5, 0.6, 0.5, 0.6, 0.6, 0.6, 0.6, 0.5, 0.6,
             0.6, 0.7, 0.7, 0.8, 0.8, 0.8, 0.7, 0.6, 0.7,
             0.7, 0.7]
        self.assertEqual(expected_gc_results, gc_results)

        # for visualization
        from matplotlib import pyplot
        pyplot.plot(gc_results)
        # pyplot.show()

    def test_relative_entropy_search(self):
        from matplotlib import pyplot
        dna_scores = c.relative_entropy_search(c.dna_seq, 6)
        protein_scores = c.relative_entropy_search(c.protein_seq, 10, is_protein=True)
        pyplot.plot(dna_scores)
        pyplot.plot(protein_scores)
        # pyplot.show()


if __name__ == "__main__":
    unittest.main()

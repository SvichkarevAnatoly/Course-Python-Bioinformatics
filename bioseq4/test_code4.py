import unittest

import alingment as a
import code4 as c


class Test(unittest.TestCase):
    def test_simple_alignment(self):
        v = "PLEASANTLY"
        w = "MEANLY"
        self.assertEqual(28, a.alignment_score(v, w))
        expected_alignment = "PLEASANTLY\n-MEA--N-LY"
        self.assertEqual(expected_alignment, a.alignment(v, w))

    def test_alignment_two_first_from_seqs(self):
        v = c.seqs[0]
        w = c.seqs[1]
        self.assertEqual(169, a.alignment_score(v, w))
        expected_alignment = "Q-PVH-PFS-RPAPVVIILIILCVMAGVIGTILLISY-GIR-LLIK\n" \
                             "QL-VHR-FTV-PAPVVIILIILCVMAGIIGTILLISYT-IRRL-IK"
        self.assertEqual(expected_alignment, a.alignment(v, w))

    def test_alignment_different_length_seqs(self):
        v = c.seqs[0]
        w = c.seqs[2]
        self.assertEqual(141, a.alignment_score(v, w))
        expected_alignment = "QPV-H-PFS-RP-APVVI-ILII--LCVMAGVIGTILLISYGIR-LL------IK------\n" \
                             "Q-LAHH-FSE-PE----IT-LIIFG--VMAGVIGTILLISYGIRRLIKKSPSDVKPLPSPD"
        self.assertEqual(expected_alignment, a.alignment(v, w))

    def test_distance_matrix(self):
        expected_dm = \
            {'s0': {'s1': 169, 's2': 141, 's3': 133, 's4': 135, 's5': 142, 's6': 116, 's7': 121, 's8': 101},
             's1': {'s0': 169, 's2': 138, 's3': 133, 's4': 132, 's5': 138, 's6': 116, 's7': 126, 's8': 103},
             's2': {'s0': 141, 's1': 138, 's3': 205, 's4': 168, 's5': 168, 's6': 156, 's7': 162, 's8': 165},
             's3': {'s0': 133, 's1': 133, 's2': 205, 's4': 169, 's5': 168, 's6': 155, 's7': 146, 's8': 153},
             's4': {'s0': 135, 's1': 132, 's2': 168, 's3': 169, 's5': 174, 's6': 148, 's7': 156, 's8': 135},
             's5': {'s0': 142, 's1': 138, 's2': 168, 's3': 168, 's4': 174, 's6': 156, 's7': 149, 's8': 132},
             's6': {'s0': 116, 's1': 116, 's2': 156, 's3': 155, 's4': 148, 's5': 156, 's7': 131, 's8': 140},
             's7': {'s0': 121, 's1': 126, 's2': 162, 's3': 146, 's4': 156, 's5': 149, 's6': 131, 's8': 141},
             's8': {'s0': 101, 's1': 103, 's2': 165, 's3': 153, 's4': 135, 's5': 132, 's6': 140, 's7': 141}}

        self.assertEqual(expected_dm, c.distance_matrix(c.seqs))

    # https://en.wikipedia.org/wiki/Neighbor_joining
    example_dm = \
        {'a': {'b': 5, 'c': 9, 'd': 9, 'e': 8},
         'b': {'a': 5, 'c': 10, 'd': 10, 'e': 9},
         'c': {'a': 9, 'b': 10, 'd': 8, 'e': 7},
         'd': {'a': 9, 'b': 10, 'c': 8, 'e': 3},
         'e': {'a': 8, 'b': 9, 'c': 7, 'd': 3}}
    example_qm = \
        {'a': {'b': -50, 'c': -38, 'd': -34, 'e': -34},
         'b': {'a': -50, 'c': -38, 'd': -34, 'e': -34},
         'c': {'a': -38, 'b': -38, 'd': -40, 'e': -40},
         'd': {'a': -34, 'b': -34, 'c': -40, 'e': -48},
         'e': {'a': -34, 'b': -34, 'c': -40, 'd': -48}}
    example_dm2 = \
        {'(a+b)': {'c': 7, 'd': 7, 'e': 6},
         'c': {'(a+b)': 7, 'd': 8, 'e': 7},
         'd': {'(a+b)': 7, 'c': 8, 'e': 3},
         'e': {'(a+b)': 6, 'c': 7, 'd': 3}}
    example_qm2 = \
        {'(a+b)': {'c': -28, 'd': -24, 'e': -24},
         'c': {'(a+b)': -28, 'd': -24, 'e': -24},
         'd': {'(a+b)': -24, 'c': -24, 'e': -28},
         'e': {'(a+b)': -24, 'c': -24, 'd': -28}}

    def test_wiki_example_distance_matrix_to_Q(self):
        qm2 = c.distance_matrix_to_q_matrix(self.example_dm)
        self.assertEqual(self.example_qm, qm2)

    def test_wiki_select_min_nodes(self):
        node1, node2 = c.select_min_nodes(self.example_qm)
        self.assertItemsEqual(['a', 'b'], [node1, node2])

    def test_wiki_delta(self):
        node1 = 'a'
        node2 = 'b'

        delta_n1_u = c.delta1(self.example_dm, node1, node2)
        expected_delta_n1_u = 2.0
        self.assertEqual(expected_delta_n1_u, delta_n1_u)

        delta_n2_u = c.delta2(self.example_dm, node1, node2, delta_n1_u)
        expected_delta_n2_u = 3.0
        self.assertEqual(expected_delta_n2_u, delta_n2_u)

    def test_wiki_new_distance_matrix(self):
        min_node1 = 'a'
        min_node2 = 'b'

        new_dm = c.new_dm(self.example_dm, min_node1, min_node2)
        self.assertEqual(self.example_dm2, new_dm)

    def test_wiki_example_new_distance_matrix_to_new_Q(self):
        qm2 = c.distance_matrix_to_q_matrix(self.example_dm2)
        self.assertEqual(self.example_qm2, qm2)

    def test_wiki_tree_construction(self):
        tree = c.construct_tree(self.example_dm)
        expected_tree = "((e+d)+(c+(a+b)))"
        self.assertEqual(expected_tree, tree)

    def test_tree_construction(self):
        dm = c.distance_matrix(c.seqs)
        tree = c.construct_tree(dm)
        expected_tree = "((((((s5+(s8+s0))+(s3+s7))+s6)+s4)+s2)+s1)"
        self.assertEqual(expected_tree, tree)

if __name__ == "__main__":
    unittest.main()

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
            [[0, 169, 141, 133, 135, 142, 116, 121, 101],
             [169, 0, 138, 133, 132, 138, 116, 126, 103],
             [141, 138, 0, 205, 168, 168, 156, 162, 165],
             [133, 133, 205, 0, 169, 168, 155, 146, 153],
             [135, 132, 168, 169, 0, 174, 148, 156, 135],
             [142, 138, 168, 168, 174, 0, 156, 149, 132],
             [116, 116, 156, 155, 148, 156, 0, 131, 140],
             [121, 126, 162, 146, 156, 149, 131, 0, 141],
             [101, 103, 165, 153, 135, 132, 140, 141, 0]]

        self.assertEqual(expected_dm, c.distance_matrix(c.seqs))

    # https://en.wikipedia.org/wiki/Neighbor_joining
    example_distance_matrix = \
        {'a': {'b': 5, 'c': 9, 'd': 9, 'e': 8},
         'b': {'a': 5, 'c': 10, 'd': 10, 'e': 9},
         'c': {'a': 9, 'b': 10, 'd': 8, 'e': 7},
         'd': {'a': 9, 'b': 10, 'c': 8, 'e': 3},
         'e': {'a': 8, 'b': 9, 'c': 7, 'd': 3}}
    example_q_matrix = \
        {'a': {'b': -50, 'c': -38, 'd': -34, 'e': -34},
         'b': {'a': -50, 'c': -38, 'd': -34, 'e': -34},
         'c': {'a': -38, 'b': -38, 'd': -40, 'e': -40},
         'd': {'a': -34, 'b': -34, 'c': -40, 'e': -48},
         'e': {'a': -34, 'b': -34, 'c': -40, 'd': -48}}

    def test_wiki_example_distance_matrix_to_Q(self):
        q_matrix = c.distance_matrix_to_q_matrix(self.example_distance_matrix)
        self.assertEqual(self.example_q_matrix, q_matrix)

    def test_select_min_nodes(self):
        node1, node2 = c.select_min_nodes(self.example_q_matrix)
        self.assertItemsEqual(['a', 'b'], [node1, node2])

    def test_delta(self):
        node1 = 'a'
        node2 = 'b'

        delta_n1_u = c.delta1(self.example_distance_matrix, node1, node2)
        expected_delta_n1_u = 2.0
        self.assertEqual(expected_delta_n1_u, delta_n1_u)

        delta_n2_u = c.delta2(self.example_distance_matrix, node1, node2, delta_n1_u)
        expected_delta_n2_u = 3.0
        self.assertEqual(expected_delta_n2_u, delta_n2_u)

    def test_new_distance_matrix(self):
        pass


if __name__ == "__main__":
    unittest.main()

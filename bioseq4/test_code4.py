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

    def test_wiki_example_distance_matrix_to_Q(self):
        # https://en.wikipedia.org/wiki/Neighbor_joining
        example_distance_matrix = \
            [[0, 5, 9, 9, 8],
             [5, 0, 10, 10, 9],
             [9, 10, 0, 8, 7],
             [9, 10, 8, 0, 3],
             [8, 9, 7, 3, 0]]
        expected_q_matrix = \
            [[0, -50, -38, -34, -34],
             [-50, 0, -38, -34, -34],
             [-38, -38, 0, -40, -40],
             [-34, -34, -40, 0, -48],
             [-34, -34, -40, -48, 0]]

        q_matrix = c.distance_matrix_to_q_matrix(example_distance_matrix)
        self.assertEqual(expected_q_matrix, q_matrix)

    if __name__ == "__main__":
        unittest.main()

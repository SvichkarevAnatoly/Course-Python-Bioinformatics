import unittest

import code as co


class Test(unittest.TestCase):
    def test_simple_consensus(self):
        seqs = ["AC", "AP"]
        consensus_str = co.consensus(seqs)
        self.assertEqual("AP", consensus_str)

if __name__ == "__main__":
    unittest.main()

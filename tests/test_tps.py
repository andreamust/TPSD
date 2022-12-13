"""
Test for TPS.
"""
import unittest

from tpsd.tps import Tps


class TestTps(unittest.TestCase):
    """
    Tests the TPS class and some of its methods.
    """

    def test_diatonic_level(self):
        """
        Tests the diatonic level of the C:maj key.
        """
        chord = Tps('C', 'C:maj')
        self.assertEqual(chord.diatonic_level(), [0, 2, 4, 5, 7, 9, 11],
                         "Diatonic level of C should be [0, 2, 4, 5, 7, 9, 11]")

    def test_triadic_level(self):
        """
        Tests the triadic level of a C:7 chord.
        """
        chord = Tps('C:7', 'C:maj')
        self.assertEqual(chord.triadic_level(), [0, 4, 7, 10],
                         "Diatonic level of C:7 should be [0, 4, 7, 9]")


if __name__ == '__main__':
    unittest.main()

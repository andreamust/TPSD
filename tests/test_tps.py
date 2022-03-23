"""
Test for TPS.
"""
import unittest

from src.tps import Tps


class TestTps(unittest.TestCase):
    """
    Tests the TPS class and some of its methods.
    """
    chord = Tps(['C', 'maj'], 'C:7')

    def test_diatonic_level(self):
        """

        :return:
        """
        self.assertEqual(self.chord.diatonic_level(), [2, 4, 5, 7, 9, 11, 0],
                         "Diatonic level of C should be [2, 4, 5, 7, 9, 11, 0]")

    def test_triadic_level(self):
        """

        :return:
        """
        self.assertEqual(self.chord.triadic_level(), [0, 4, 7, 10],
                         "Diatonic level of C should be [0, 4, 7, 9]")


if __name__ == '__main__':
    unittest.main()

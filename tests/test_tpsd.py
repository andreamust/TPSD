"""
Test for TPSD.
"""
import unittest

from src.tpsd import Tpsd


class TestTpsd(unittest.TestCase):
    """
    Tests the Tpsd class and some of its methods.
    """
    chord = Tpsd(chord_a='C', key_a=['C', 'maj'], chord_b='C#', key_b=['C#', 'maj'])

    def test_distance(self):
        """
        Tests the distance value given two chords.
        """
        self.assertEqual(self.chord.distance(), 14,
                         "Distance between C and C# should be 14")


if __name__ == '__main__':
    unittest.main()

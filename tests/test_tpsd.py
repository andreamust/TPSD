import unittest

from src.tpsd import Tpsd


class TestTPSD(unittest.TestCase):
    """
    Tests the Tpsd class and some of its methods.
    """
    chord = Tpsd(chord_a='C', key_a='C', chord_b='C#', key_b='C#')

    def test_distance(self):
        """
        Tests the distance value given two chords.
        """
        self.assertEqual(self.chord.distance(), 11,
                         "Distance between C and C# should be 11")


if __name__ == '__main__':
    unittest.main()

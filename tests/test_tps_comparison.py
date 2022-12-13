"""
Test for TPS comparing two chords.
"""
import unittest

from tpsd.tps_comparison import TpsComparison


class TestTpsComparison(unittest.TestCase):
    """
    Tests the TpsComparison class and some of its methods.
    """

    # pylint: disable=line-too-long

    def test_distance(self):
        """
        Tests the distance C and G7 (C:maj key) as shown in Table 2
        (De Haas et al. 2008).
        """
        chord = TpsComparison(chord_a='C', key_a='C:maj', chord_b='G:7',
                              key_b='C:maj')
        self.assertEqual(chord.distance(), 5.5,
                         "Distance between C and G:7 in C:maj should be 5.5")

    def test_distance_2(self):
        """
        Tests distance between D and D:min (D:maj key) as shown in Table 3
        (De Haas et al. 2008).
        """
        chord_2 = TpsComparison(chord_a='D', key_a='D:maj', chord_b='D:min',
                                key_b='D:maj')
        self.assertEqual(chord_2.distance(), 1.5,
                         "Distance between D and D:min in D:maj should be 1.5")

    def test_distance_3(self):
        """
        Tests distance between two identical chords in the same key.
        """
        chord_3 = TpsComparison(chord_a='F', key_a='G:maj', chord_b='F',
                                key_b='G:maj')
        self.assertEqual(chord_3.distance(), 0,
                         "Distance between F and F in C:maj should be 0")

    def test_distance_4(self):
        """
        Tests distance between C:maj and E containing all pitch classes as shown
        in Table 4 (De Haas et al. 2008).
        """
        chord_4 = TpsComparison(chord_a='C', key_a='C:maj',
                                chord_b='E:(b2,2,b3,b4,4,b5,5,b6,6,b7,7)',
                                key_b='E:maj')
        self.assertEqual(chord_4.distance(), 13.0,
                         "Distance between C and E:(b2,2,b3,b4,4,b5,5,b6,6,b7,7)"
                         " in C:maj should be 13")

    def test_distance_5(self):
        """
        Tests distance between two identical chords in the same key as shown in
        Table 5.a (De Haas et al. 2013).
        """
        chord_5 = TpsComparison(chord_a='A:min', key_a='C:Maj', chord_b='A:min',
                                key_b='C:maj')
        self.assertEqual(chord_5.distance(), 0,
                         "Distance between A:min and A:min in C:maj should be 0")

    def test_chord_distance_rule(self):
        """
        Tests chord distance rule between C and C# containing all pitch classes,
        as shown in Table 5.b
        (De Haas et al. 2013).
        """
        chord_6 = TpsComparison(chord_a='C', key_a='C:maj',
                                chord_b='C#:(b2,2,b3,b4,4,b5,5,b6,6,b7,7)',
                                key_b='C:maj')
        self.assertEqual(chord_6.chord_distance_rule(), 20,
                         "Chord distance rule between C:maj and "
                         "C#:(b2,2,b3,b4,4,b5,5,b6,6,b7,7) in C:maj should be 20")


if __name__ == '__main__':
    unittest.main()

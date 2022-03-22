import unittest

from src.TPSD import TPSD


class TestTPSD(unittest.TestCase):
    chord = TPSD(chord_a='C', key_a='C', chord_b='C#', key_b='C#')

    def test_distance(self):
        self.assertEqual(self.chord.get_distance(), 11,
                         "Distance between C and C# should be 11")


if __name__ == '__main__':
    unittest.main()

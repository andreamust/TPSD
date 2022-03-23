"""
This script contains a Python 3 re-implementation of the Tonal Pith Space Distance (TPSD) algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a similarity measure for chord progressions.
In: ISMIR. pp. 51–56 (2008)
"""
from src.tpsd import Tpsd


def parse_sequence():
    """
    Parses a chord sequence and returns the overall TPSD value.
    :return:
    """
    return None


if __name__ == '__main__':
    tpsd = Tpsd(chord_a='C', key_a=['C', 'maj'], chord_b='C', key_b=['C', 'maj'])
    tpsd.plot()
    print(tpsd.distance())
    print(f'fifthsRule: {tpsd.circle_fifth_rule()}\nchordDistanceRule: {tpsd.chord_distance_rule()}')

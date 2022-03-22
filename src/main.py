"""
This script contains a Python 3 re-implementation of the Tonal Pith Space Distance (TPSD) algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a similarity measure for chord progressions.
In: ISMIR. pp. 51–56 (2008)
"""
from TPSD import TPSD


def parse_song():
    pass


if __name__ == '__main__':
    tpsd = TPSD(chord_a='C', key_a=['C', 'maj'], chord_b='G:7', key_b=['C', 'maj'], show=True)
    tpsd.plot()
    print(tpsd.chord_distance_rule())

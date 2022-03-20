"""
This script contains a Python 3 re-implementation of the Tonal Pith Space Distance (TPSD) algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a similarity measure for chord progressions. In: ISMIR. pp. 51–56 (2008)
"""
import TPSD


def parse_song():
    pass


if __name__ == '__main__':
    tpsd = TPSD.TPSD(chord_a=['C', 'E', 'G'], key_a='C', chord_b=['C#', 'F', 'G#'], key_b='C#', show=True)
    print(tpsd.get_distance())
    tpsd.plot()

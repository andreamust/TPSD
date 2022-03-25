# pylint: disable=line-too-long
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
    # pylint: disable=line-too-long
    tpsd = Tpsd(['A', 'G:7', 'E', 'C#', 'Db', 'C:min'], 'C:maj')
    print(tpsd.sequence_area())
    tpsd.plot_area()

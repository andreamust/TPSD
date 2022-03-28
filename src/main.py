# pylint: disable=line-too-long
"""
This script contains a Python 3 re-implementation of the Tonal Pith Space Distance (TPSD) algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a similarity measure for chord progressions.
In: ISMIR. pp. 51–56 (2008)

Author: Andrea Poltronieri (University of Bologna) and Jacopo de Berardinis (King's College of London)
Copyright: 2022 Andrea Poltronieri and Jacopo de Berardinis
License: MIT license
"""
from src.tpsd import Tpsd
from src.util import *


def parse_sequence():
    """
    Parses a chord sequence and returns the overall TPSD value.
    :return:
    """
    return None


if __name__ == '__main__':
    # pylint: disable=line-too-long
    chord_sequence = open_harte('../test_data/allTheThingsYouAre.txt')
    print(chord_sequence)
    tpsd = Tpsd(chord_sequence, 'C:maj')
    print(tpsd.sequence_area())
    tpsd.plot_area()

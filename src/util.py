# pylint: disable=line-too-long
"""
This file contains utility functions to support the implementation of the Tonal Pitch Step Distance (TPSD) algorithm
as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a similarity measure for chord progressions.
In: ISMIR. pp. 51–56 (2008)

Author: Andrea Poltronieri (University of Bologna) and Jacopo de Berardinis (King's College of London)
Copyright: 2022 Andrea Poltronieri and Jacopo de Berardinis
License: MIT license
"""


def open_harte(harte_file_path: str) -> list[str]:
    """
    Utility function that given a file containing chords notation encoded using the Harte notation, returns a list of
    the chords contained in the file
    :param harte_file_path: the path where the file is stored
    :return: a list of string, where each string corresponds to a chord.
    """
    with open(harte_file_path, 'r') as harte_file:
        return [line.replace('\n', '').replace('hdim', 'hdim7') for line in harte_file]

# pylint: disable=line-too-long
"""
This script contains a Python 3 re-implementation of the Tonal Pith Space
Distance (TPSD) algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a
similarity measure for chord progressions.
In: ISMIR. pp. 51–56 (2008)

Author: Andrea Poltronieri (University of Bologna) and Jacopo de Berardinis
(King's College of London)
Copyright: 2022 Andrea Poltronieri and Jacopo de Berardinis
License: MIT license
"""
from tpsd.tps_comparison import TpsComparison
from tpsd.tpsd_core import Tpsd
from tpsd.tpsd_comparison import TpsdComparison
from tpsd.util import open_harte, parse_mgu, get_corresponding_biab

DATASET_PATH = '../tests/dump_dataset'
TEST_FILE_A = '../tests/test_data/All The Things You Are_id_07051_allanah.MGU.txt'
TEST_FILE_B = '../tests/test_data/All The Things You Are_id_00123_community.MGU.txt'


def parse_sequence():
    """
    Parses a chord sequence and returns the overall TPSD value.
    :return:
    """
    return None


if __name__ == '__main__':
    # pylint: disable=line-too-long

    # SHOWCASE OF THE METHODS IMPLEMENTED IN THIS LIBRARY

    # PREPARE DATA
    ###############
    # gets the chord sequence and the key opening the .txt file containing the
    # Harte annotations
    chord_sequence_a, key_a = open_harte(TEST_FILE_A)
    chord_sequence_b, key_b = open_harte(TEST_FILE_B)
    # gets the timing information by parsing a Band-in-a-Box file.
    # It searches automatically for the correct file if the path of the dataset
    # and the filename are given
    timing_info_a = parse_mgu(get_corresponding_biab(TEST_FILE_A, DATASET_PATH))
    timing_info_b = parse_mgu(get_corresponding_biab(TEST_FILE_B, DATASET_PATH))

    # TPS EXPERIMENTS
    #################
    # given two chords and two keys computes the TPS on them
    tps_comparison = TpsComparison('C:maj', 'C:maj', 'D:min7', 'C:maj')
    # calculates the circle-of-fifth-rule, which is a constituent part of the
    # TPS function
    # print(tps_comparison.circle_fifth_rule())
    # generates a table plot for the TPS
    # tps_comparison.plot()

    # TPSD CALCULATION
    ##################
    # calculates the TPSD area given a chord sequence, a key and the duration
    # for each chord (in beats)
    tpsd = Tpsd(chord_sequence_b, key_b, timing_info_b)
    # plots the TPSD area of a chord sequence
    # tpsd.plot_area()

    # TPSD COMPARISON
    #################
    # calculates the TPSD among two chord sequences
    tpsd_comparison = TpsdComparison(chord_sequence_a, chord_sequence_b, key_a,
                                     key_b, timing_info_a, timing_info_b)
    tpsd_comparison.plot_area()
    # compute the minimum area
    print(tpsd_comparison.minimum_area())

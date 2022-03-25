# pylint: disable=line-too-long
"""
This script contains a Python 3 re-implementation of the Tonal Pith Space Distance (TPSD) algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a similarity measure for chord progressions.
In: ISMIR. pp. 51–56 (2008)
"""
import matplotlib.pyplot as plt
import numpy as np

from src.tps_comparison import TpsComparison


class Tpsd:
    """
    Implements the TPS as described in De Haas et al.
    """

    # pylint: disable=line-too-long
    # pylint: disable=consider-using-enumerate
    def __init__(self, chord_sequence: list[str], key: str):
        """
        Initialises the parameters needed for calculating the TPSD distance
        :param chord_sequence: a list of chords expressed using the Harte notation
        :param key: the key of the chord sequence to which calculate the sequence distance.
        """
        self.key = key
        self.chord_sequence = chord_sequence

    def sequence_area(self):
        tpsd = []
        for chord in self.chord_sequence:
            chord_tpsd = TpsComparison(chord_a=chord, key_a=self.key, chord_b=self.key, key_b=self.key)
            tpsd.append(chord_tpsd.distance())

        return tpsd

    def plot_area(self):
        plt.step([x + 1 for x in range(len(self.sequence_area()))], self.sequence_area())
        plt.yticks(np.arange(0, 13 + 1))
        plt.xticks(np.arange(0, len(self.sequence_area())))
        plt.xlabel(self.chord_sequence)

        plt.show()

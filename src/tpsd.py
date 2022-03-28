# pylint: disable=line-too-long
"""
This script contains a Python 3 re-implementation of the Tonal Pith Space Distance (TPSD) algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a similarity measure for chord progressions.
In: ISMIR. pp. 51–56 (2008)

Author: Andrea Poltronieri (University of Bologna) and Jacopo de Berardinis (King's College of London)
Copyright: 2022 Andrea Poltronieri and Jacopo de Berardinis
License: MIT license
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
    def __init__(self, chord_sequence: list[str], key: str) -> None:
        """
        Initialises the parameters needed for calculating the TPSD distance
        :param chord_sequence: a list of chords expressed using the Harte notation
        :param key: the key of the chord sequence to which calculate the sequence distance.
        """
        self.key = key
        self.chord_sequence = chord_sequence

    def sequence_area(self) -> list[float]:
        """
        Calculates the TPS distance between all chords of a given sequence and the triad chord of a given key
        :return: a list of all the TPS distances calculated between all the chord in the input sequence and the triad
        of the global key.
        """
        tpsd = []
        for chord in self.chord_sequence:
            print(chord)
            chord_tpsd = TpsComparison(chord_a=chord, key_a=self.key, chord_b=self.key, key_b=self.key)
            tpsd.append(chord_tpsd.distance())

        return tpsd

    def plot_area(self) -> None:
        """
        Plots the area calculated applying the TPS algorithm on a chord sequence
        :return: None but plots the area defined by the TPSD.
        """
        sequence = self.sequence_area()
        # sequence.insert(0, sequence[0])

        y = sequence
        x = range(len(sequence))
        plt.step(x, y, 'orange')
        plt.yticks(np.arange(0, 13 + 1))
        plt.xticks(np.arange(0, len(sequence)))
        plt.ylabel('TPS score')
        plt.xlabel('Beat')

        plt.fill_between(x, y, step='pre', color='orange', alpha=0.4)

        plt.show()

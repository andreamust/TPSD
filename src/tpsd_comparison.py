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

from src.tpsd import Tpsd


class TpsdComparison:
    """
        Implements the TPSD as described in De Haas et al.
        """

    # pylint: disable=line-too-long
    # pylint: disable=consider-using-enumerate
    def __init__(self, chord_sequence_a: list[str], chord_sequence_b: list[str], key_a: str, key_b: str,
                 duration_sequence_a: list[int], duration_sequence_b: list[int]) -> None:
        """
        Implementation of the comparison between two TPSD distances
        :param chord_sequence_a:
        :param chord_sequence_b:
        :param key_a:
        :param key_b:
        :param duration_sequence_a:
        :param duration_sequence_b:
        """
        tpsd_a = Tpsd(chord_sequence_a, key_a, duration_sequence_a)
        tpsd_b = Tpsd(chord_sequence_b, key_b, duration_sequence_b)
        self.sequence_area_a = tpsd_a.sequence_area()
        self.sequence_area_b = tpsd_b.sequence_area()

    def plot_area(self) -> None:
        """

        :return: None
        """
        sequence_a = self.sequence_area_a
        sequence_b = self.sequence_area_b

        plt.step(range(len(sequence_a)), sequence_a, 'orange')
        plt.step(range(len(sequence_b)), sequence_b, 'red')
        plt.yticks(np.arange(0, 13 + 1))
        plt.xticks(np.linspace(0, len(sequence_a), 15, dtype=int))
        plt.ylabel('TPS score')
        plt.xlabel('Beat')

        plt.fill_between(range(len(sequence_a)), sequence_a, step='pre', color='orange', alpha=0.4)
        plt.fill_between(range(len(sequence_b)), sequence_b, step='pre', color='red', alpha=0.4)

        plt.show()

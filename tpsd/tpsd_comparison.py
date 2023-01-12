# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
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
from typing import Union

import matplotlib.pyplot as plt
import numpy as np

from tpsd.tpsd_core import Tpsd


class TpsdComparison:
    """
    Implements the TPSD as described in De Haas et al.
    """

    # pylint: disable=line-too-long
    # pylint: disable=consider-using-enumerate
    def __init__(self, chord_sequence_a: list[str],
                 chord_sequence_b: list[str],
                 key_a: Union[str, list[str]],
                 key_b: Union[str, list[str]],
                 duration_sequence_a: list[int],
                 duration_sequence_b: list[int]) -> None:
        """
        Implementation of the comparison between two TPSD distances
        :param chord_sequence_a: the first sequence of chord to be compared
        :type chord_sequence_a: list[str]
        :param chord_sequence_b: the second sequence of chord to be compared
        :type chord_sequence_b: list[str]
        :param key_a: the key(s) of the first sequence of chord to be compared
        :type key_a: Union[str, list[str]]
        :param key_b: the key(s) of the second sequence of chord to be compared
        :type key_b: Union[str, list[str]]
        :param duration_sequence_a: the duration information of the first
        sequence of chord to be compared
        :type duration_sequence_a: list[int]
        :param duration_sequence_b: the duration information of the second
        sequence of chord to be compared
        :type duration_sequence_b: list[int]
        :return: None
        """
        tpsd_a = Tpsd(chord_sequence_a, key_a, duration_sequence_a)
        tpsd_b = Tpsd(chord_sequence_b, key_b, duration_sequence_b)
        self.sequence_area_a = tpsd_a.sequence_area()
        self.sequence_area_b = tpsd_b.sequence_area()

        self.longest_sequence = self.sequence_area_a if len(
            self.sequence_area_a) >= len(
            self.sequence_area_b) else self.sequence_area_b
        self.shortest_sequence = self.sequence_area_a if len(
            self.sequence_area_a) <= len(
            self.sequence_area_b) else self.sequence_area_b

    def plot_area(self) -> None:
        """
        Plots the areas of the two sequences overlapped, showing intersections
        between the two areas
        :return: None, but plots a matplotlib graph
        """
        sequence_a = self.sequence_area_a
        sequence_b = self.sequence_area_b

        plt.step(range(len(sequence_a)), sequence_a, 'orange',
                 label='sequence_1')
        plt.step(range(len(sequence_b)), sequence_b, 'red', label='sequence_2')
        plt.yticks(np.arange(0, 14))
        plt.xticks(np.linspace(0, len(self.longest_sequence), 15, dtype=int))
        plt.ylabel('TPS score')
        plt.xlabel('Beats')
        plt.legend(loc='upper left')
        plt.fill_between(range(len(sequence_a)), sequence_a, step='pre',
                         color='orange', alpha=0.4)
        plt.fill_between(range(len(sequence_b)), sequence_b, step='pre',
                         color='red', alpha=0.4)

        plt.show()

    def minimum_area(self) -> float:
        """
        Calculates the minimum area between the step functions calculated over
        two chord sequences
        :return: a floating number which corresponds to the value of minimum
        area between the two areas
        """
        minimum_area = 0
        longest = self.longest_sequence[:]
        for step in range(
                len(self.longest_sequence) - len(self.shortest_sequence) + 1):
            if step != 0:
                longest.pop(0)
            area = 0
            for beat in range(len(self.shortest_sequence)):
                lower = self.shortest_sequence[beat] if self.shortest_sequence[
                                                            beat] <= longest[
                                                            beat] else \
                    longest[beat]
                higher = self.shortest_sequence[beat] if self.shortest_sequence[
                                                             beat] > longest[
                                                             beat] else \
                    longest[beat]

                area += higher - lower
            if minimum_area > area or step == 0:
                minimum_area = area
        return minimum_area / len(self.shortest_sequence)

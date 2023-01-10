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
from typing import Union

import matplotlib.pyplot as plt
import numpy as np

from tpsd.tps_comparison import TpsComparison


class Tpsd:
    """
    Implements the TPSD as described in De Haas et al.
    """

    # pylint: disable=line-too-long
    # pylint: disable=consider-using-enumerate
    def __init__(self, chord_sequence: list[str], keys: Union[str, list[str]],
                 timing_information: list[int]) -> None:
        """
        Initialises the parameters needed for calculating the TPSD distance
        :param chord_sequence: a list of chords expressed using the Harte
        notation
        :param keys: the keys of the chord sequence to which calculate the
        sequence distance.
        """
        if isinstance(keys, str):  # creating a local key vector
            keys = [keys] * len(chord_sequence)
        if len(chord_sequence) != len(timing_information) != len(keys):
            raise ValueError("Size mismatch: cannot compute TSPD profile")

        self.keys = keys
        self.chord_sequence = chord_sequence
        self.timing_information = timing_information

    def sequence_area(self) -> list[float]:
        """
        Calculates the TPS distance between all chords of a given sequence and
        the triad chord of a given key
        :return: a list of all the TPS distances calculated between all the
        chord in the input sequence and the triad
        of the global key.
        """
        tpsd = []
        for idx, (chord, key) in enumerate(zip(self.chord_sequence, self.keys)):
            chord_tpsd = TpsComparison(chord_a=chord, key_a=key, chord_b=key,
                                       key_b=key)
            for _ in range(self.timing_information[idx]):
                tpsd.append(chord_tpsd.distance())

        return tpsd

    def plot_area(self, **fig_kwargs) -> tuple[plt.Figure, plt.Axes]:
        """
        Plots the area calculated applying the TPS algorithm on a chord sequence
        :return: None but plots the area defined by the TPSD.
        """
        sequence = self.sequence_area()
        # sequence.insert(0, sequence[0])
        fig, axis = plt.subplots(**fig_kwargs)

        axis.step(range(len(sequence)), sequence, 'orange')
        axis.set_yticks(np.arange(0, 13 + 1))
        axis.set_xticks(np.linspace(0, len(sequence), 15, dtype=int))
        axis.set_ylabel('TPS score')
        axis.set_xlabel('Beat')

        axis.fill_between(range(len(sequence)), sequence,
                        step='pre', color='orange', alpha=0.4)
        plt.show()

        return fig, axis

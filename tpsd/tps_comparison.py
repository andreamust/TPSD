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
from tabulate import tabulate
from termcolor import colored

from tpsd.tps import Tps


class TpsComparison:
    """
    Implements the TPS as described in De Haas et al.
    """

    # pylint: disable=line-too-long
    # pylint: disable=consider-using-enumerate
    def __init__(self, chord_a: str, key_a: str, chord_b: str, key_b: str):
        """
        Computes argument from TPS and organises them in a coherent manner
        :param chord_a: first chord to compare
        :param key_a: key of the first chord
        :param chord_b: second chord to compare
        :param key_b: key of the second chord
        """
        self.chord_a = Tps(key=key_a, chord=chord_a)
        self.chord_b = Tps(key=key_b, chord=chord_b)

        self.tps_a = self.chord_a.get_levels()
        self.tps_b = self.chord_b.get_levels()

    def get_tpsd_distance(self) -> int:
        """
        Computes the TPSD distance between two given chords and their respective
         tonalities.
        :return: the distance value that results from the comparison of the two
        chords.
        """
        distance = 0
        for i in range(len(self.tps_a)):
            distance += len(list(set(self.tps_a[i]) - set(self.tps_b[i])))
        return distance

    def circle_fifth_rule(self) -> int:
        """
        Implements the circle of fifth rule (Lehrdal et al.).
        :return: the resulting value of the circle of fifths rule
        (int from 1 to 3).
        """
        diatonic_fifths_ascending = [0, 7, 2, 9]
        diatonic_fifths_descending = [5, 11, 4]

        if self.chord_b.root_level()[0] - self.chord_a.root_level()[
            0] in diatonic_fifths_ascending:
            return diatonic_fifths_ascending.index(
                self.chord_b.root_level()[0] - self.chord_a.root_level()[0])
        if self.chord_b.root_level()[0] - self.chord_a.root_level()[
            0] in diatonic_fifths_descending:
            return diatonic_fifths_descending.index(
                self.chord_b.root_level()[0] - self.chord_a.root_level()[0]) + 1
        return 3

    def chord_distance_rule(self) -> float:
        """
        Computes the TPS distance between two given chords.
        :return: the distance value that results from the comparison of the two
        chords, which is the number of grades
        that do not correspond between all the TPS levels of the two chord taken
        into account.
        """
        tps_distance = 0

        for i in range(len(self.tps_a)):
            tps_distance += len(
                set(self.tps_a[i]).symmetric_difference(set(self.tps_b[i])))
        return tps_distance

    def distance(self) -> float:
        """
        Computes the total TPSD distance taking into account the Circle of Fifth
        rule and the Chord Distance Rule.
        :return: a floating number which is the final value of the TPS between
        two chords.
        """
        return (self.chord_distance_rule() / 2) + self.circle_fifth_rule()

    def plot(self) -> None:
        """
        Plots the TPSD distance in a graphical way
        :return : None
        """
        print('Plot of the first chord')
        self.chord_a.show_table()
        print('Plot of the second chord')
        self.chord_b.show_table()

        plot_level_a = self.chord_a.prepare_show()
        plot_level_b = self.chord_b.prepare_show()
        final_plot = []
        for i, level in enumerate(plot_level_a):
            plot_b = plot_level_b[i]
            final_plot.append(
                [x if x == plot_b[idx] else (colored(str(plot_b[idx]), 'red',
                                                     attrs=[
                                                         'bold'])) if x == '_' else (
                    colored(str(x), 'red', attrs=['bold'])) for idx, x in
                 enumerate(level)])

        print('TPSD plot\n', tabulate(final_plot))

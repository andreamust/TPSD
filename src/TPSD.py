"""
This script contains a Python 3 re-implementation of the Tonal Pith Space Distance (TPSD) algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a similarity measure for chord progressions. In: ISMIR. pp. 51–56 (2008)
"""
import TPS
from tabulate import tabulate


class TPSD:
    def __init__(self, chord_a: list[str], key_a: str, chord_b: list[str], key_b: str, show: bool = False):
        """
        Computes argument from TPS and organises them in a coherent manner
        :param chord_a: first chord to compare
        :param key_a: key of the first chord
        :param chord_b: second chord to compare
        :param key_b: key of the second chord
        """
        self.chord_a = TPS.TPS(key=key_a, chord=chord_a, show=show)
        self.chord_b = TPS.TPS(key=key_b, chord=chord_b, show=show)

        self.tps_a = [self.chord_a.root_level(), self.chord_a.fifth_level(), self.chord_a.triadic_level(),
                      self.chord_a.diatonic_level()]
        self.tps_b = [self.chord_b.root_level(), self.chord_b.fifth_level(), self.chord_b.triadic_level(),
                      self.chord_b.diatonic_level()]
        if show:
            print('Plot of the first chord')
            self.chord_a.show_table()
            print('Plot of the second chord')
            self.chord_b.show_table()

    def get_distance(self) -> int:
        """
        Computes the TPSD distance between two given chords and their respective tonalities.
        :return: the distance value that results from the comparison of the two chords.
        """
        distance = 0
        for i in range(len(self.tps_a)):
            distance += len(list(set(self.tps_a[i]) - set(self.tps_b[i])))
        return distance

    def plot(self):
        plot_level_a = self.chord_a.prepare_show()
        plot_level_b = self.chord_b.prepare_show()
        final_plot = []
        for i, level in enumerate(plot_level_a):
            y = plot_level_b[i]
            final_plot.append([x if x == y[idx] else ((str(y[idx])) if x == '_' else (str(x))) for idx, x in enumerate(level)])

        print('TPSD plot\n', tabulate(final_plot))

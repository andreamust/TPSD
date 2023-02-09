"""
This script contains a Python 3 re-implementation of the Tonal Pith Space (TPS)
algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a
similarity measure for chord progressions.
In: ISMIR. pp. 51–56 (2008)

Author: Andrea Poltronieri (University of Bologna) and Jacopo de Berardinis
(King's College of London)
Copyright: 2022 Andrea Poltronieri and Jacopo de Berardinis
License: MIT license
"""
from typing import List

from harte.harte import Harte
from tabulate import tabulate

KEYS = {
    'maj': [2, 2, 1, 2, 2, 2, 1],
    'min': [2, 1, 2, 2, 1, 2, 2],
    'dor': [2, 1, 2, 2, 2, 1, 2],
    'mix': [2, 2, 1, 2, 2, 1, 2],
    'lyd': [2, 2, 2, 1, 2, 2, 1],
    'phr': [1, 2, 2, 2, 1, 2, 2],
    'loc': [2, 2, 1, 2, 2, 2, 1],
}


class Tps:
    """
    Implements the preliminary methods of the TPS approach proposed by Lehrdal.
    """
    chromatic_level = list(range(0, 12))

    def __init__(self, chord: str, key: str):
        if ':' not in key:
            key += ':maj'
        key_root, key_mode = key.split(':')
        key_mode = key_mode[:3].lower()
        assert key_mode in KEYS, 'The entered key mode is not valid.'
        self.scale_grades = KEYS[key_mode]
        self.key = key_root if key_root != '' else chord.split(':')[0]
        self._chord = Harte(chord)
        self.tones = tuple(sorted(self._chord.pitchClasses))

    @staticmethod
    def note_index(note) -> int:
        """
        Gets a note label and returns its index within the chromatic scale.
        :return: the index of the note within the chromatic scale.
        """
        note_map = [
            ('C', 'Dbb', 'B#'),
            ('C#', 'Db'),
            ('D', 'C##', 'Ebb'),
            ('Eb', 'D#'),
            ('E', 'D##', 'Fb'),
            ('F', 'E#', 'Gbb'),
            ('F#', 'Gb'),
            ('G', 'F##', 'Abb'),
            ('G#', 'Ab'),
            ('A', 'G##', 'Bbb'),
            ('Bb', 'A#'),
            ('B', 'A##', 'Cb')
        ]

        try:
            return [i for i, n in enumerate(note_map) if note in n][0]
        except IndexError as exc:
            raise NameError(
                'The note is not indexed, try with an enharmonic') from exc

    def diatonic_level(self) -> List[int]:
        """
        Computes the diatonic level of the TPS.
        :return: a list of the grades belonging to the diatonic level of the TPS
        """
        note_index = self.note_index(self.key)
        diatonic_grades = list(self.tones)
        for grade in self.scale_grades:
            note_index = (note_index + grade)
            if note_index >= 12:
                note_index = note_index - 12
            diatonic_grades.append(note_index)
        return list(set(diatonic_grades))

    def triadic_level(self) -> List[int]:
        """
        Computes the triadic level of the TPS. Contrary to what the name might
        suggest, the method calculates the
        grades of all notes in the chord.
        :return: a list of the grades belonging to the triadic level of the TPS.
        """
        return list(self.tones)

    def root_level(self) -> List[int]:
        """
        Computes the root level of the TPS.
        :return: a list of the grades belonging to the root level of the TPS.
        """
        return [self._chord.root().pitchClass]

    def fifth_level(self) -> List[int]:
        """
        Computes the fifth level of the TPS.
        :return: a list of the grades belonging to the fifth level of the TPS.
        """
        root = self._chord.root().pitchClass
        fifth = root + 7 if root + 7 < 12 else root + 7 - 12
        return [root, fifth]

    def get_levels(self):
        """
        Merges all levels of TPS.
        :return: a list of all levels of the TPS.
        """
        return [self.diatonic_level(), self.triadic_level(), self.fifth_level(),
                self.root_level()]

    def prepare_show(self) -> List:
        """
        Prepares the data to be plotted.
        :return: A list of lists containing the missing grades, replaced with
        the placeholder "_".
        :rtype: List
        """
        show_levels = [self.chromatic_level,
                       ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A',
                        'Bb', 'B']]
        for level in self.get_levels():
            show_levels.insert(0, [grade if grade in level else '_' for grade in
                                   self.chromatic_level])
        return show_levels

    def show_table(self) -> None:
        """
        Prints a table of the TPS if the show parameter is set to True when
        initialising the class.
        :return: None
        """
        print(tabulate(self.prepare_show()))


if __name__ == '__main__':
    # test the class
    chord = Tps(key='C', chord='N')
    chord.show_table()

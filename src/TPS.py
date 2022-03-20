"""
This script contains a Python 3 re-implementation of the Tonal Pith Space (TPS) algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a similarity measure for chord progressions. In: ISMIR. pp. 51–56 (2008)
"""
from tabulate import tabulate


class TPS:
    chromatic_level = list(range(0, 12))

    def __init__(self, key: str, chord: list[str], scale_grades: list[str] = None, show: bool = None):
        if scale_grades is None:
            self.scale_grades = [2, 2, 1, 2, 2, 2, 1]
        self.key = key.upper()
        self.chord = chord
        self.show = show

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
        except IndexError:
            raise NameError('The note is not indexed, try with enharmonics.')

    def diatonic_level(self):
        """
        Computes the diatonic level of the TPS.
        :return: a list of the grades belonging to the diatonic level of the TPS.
        """
        note_index = self.note_index(self.key)
        diatonic_grades = []
        for grade in self.scale_grades:
            note_index = (note_index + grade)
            if note_index >= 12:
                note_index = note_index - 12
            diatonic_grades.append(note_index)
        return diatonic_grades

    def triadic_level(self):
        """
        Computes the triadic level of the TPS. Contrary to what the name might suggest, the method calculates the
        grades of all notes in the chord.
        :return: a list of the grades belonging to the triadic level of the TPS.
        """
        triadic_grades = []

        for note in self.chord:
            chord_note_index = self.note_index(note)
            triadic_grades.append(chord_note_index)
        return triadic_grades

    def root_level(self):
        """
        Computes the root level of the TPS.
        :return: a list of the grades belonging to the root level of the TPS.
        """
        root = self.note_index(self.chord[0])
        return [root]

    def fifth_level(self):
        """
        Computes the fifth level of the TPS.
        :return: a list of the grades belonging to the fifth level of the TPS.
        """
        fifth = self.note_index(self.chord[0]) + 7 if self.note_index(self.chord[0]) + 7 < 12 else self.note_index(
            self.chord[0]) + 7 - 12
        fifth_grades = [self.note_index(self.chord[0]), fifth]
        return fifth_grades

    def show_table(self):
        """
        Prints a table of the TPS if the show parameter is set to True when initialising the class.
        """
        if self.show:
            show_levels = [self.chromatic_level, ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']]
            for level in [self.root_level(), self.fifth_level(), self.triadic_level(), self.diatonic_level()][::-1]:
                show_levels.insert(0, [grade if grade in level else '_' for grade in self.chromatic_level])

            print(tabulate(show_levels))
        else:
            pass

# chord = TPS(key='C', chord=['C', 'E', 'G'], show=True)
# chord.show_table()

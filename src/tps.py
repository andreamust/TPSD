# pylint: disable=line-too-long
"""
This script contains a Python 3 re-implementation of the Tonal Pith Space (TPS) algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a similarity measure for chord progressions.
In: ISMIR. pp. 51–56 (2008)
"""
from chord_labels import parse_chord
from tabulate import tabulate


class Tps:
    """
    Implements the preliminary methods of the TPS approach proposed by Lehrdal.
    """
    # pylint: disable=line-too-long
    chromatic_level = list(range(0, 12))

    def __init__(self, key: list[str], chord: str):
        if key[1] == 'maj':
            self.scale_grades = [2, 2, 1, 2, 2, 2, 1]
        elif key[1] == 'min':
            self.scale_grades = [2, 1, 2, 2, 1, 2, 2]
        else:
            raise NameError('The only two scale grades accepted are "min" and "maj".')

        self.key = key[0].upper()
        self.chord = parse_chord(chord)

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

    def diatonic_level(self) -> list[int]:
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

    def triadic_level(self) -> list[int]:
        """
        Computes the triadic level of the TPS. Contrary to what the name might suggest, the method calculates the
        grades of all notes in the chord.
        :return: a list of the grades belonging to the triadic level of the TPS.
        """
        return self.chord.tones

    def root_level(self) -> list[int]:
        """
        Computes the root level of the TPS.
        :return: a list of the grades belonging to the root level of the TPS.
        """
        return [self.chord.root]

    def fifth_level(self) -> list[int]:
        """
        Computes the fifth level of the TPS.
        :return: a list of the grades belonging to the fifth level of the TPS.
        """
        fifth = self.chord.root + 7 if self.chord.root + 7 < 12 else self.chord.root + 7 - 12
        fifth_grades = [self.chord.root, fifth]
        return fifth_grades

    def get_levels(self):
        """
        Merges all levels of TPS.
        :return: a list of all levels of the TPS.
        """
        return [self.diatonic_level(), self.triadic_level(), self.fifth_level(), self.root_level()]

    def prepare_show(self) -> list:
        """
        Prepares the data to be plotted.
        :return: A list of lists containing the missing grades, replaced with the placeholder "_".
        """
        show_levels = [self.chromatic_level, ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']]
        for level in self.get_levels():
            show_levels.insert(0, [grade if grade in level else '_' for grade in self.chromatic_level])
        return show_levels

    def show_table(self) -> None:
        """
        Prints a table of the TPS if the show parameter is set to True when initialising the class.
        """
        print(tabulate(self.prepare_show()))

# chord = TPS(key='C', chord='C', show=True)
# chord.show_table()

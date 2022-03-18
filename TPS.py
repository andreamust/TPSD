"""
This script contains a Python 3 re-implementation of the Tonal Pith Space (TPS) algorithm as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a similarity measure for chord progressions. In: ISMIR. pp. 51–56 (2008)
"""


class TPS:
    chromatic_level = list(range(0, 12))

    def __init__(self, key: str, chord: list, scale_grades: list = None, show: bool = None):
        if scale_grades is None:
            self.scale_grades = [2, 2, 1, 2, 2, 2, 1]
        self.key = key.upper()
        self.chord = chord
        self.show = show

    def note_index(self) -> int:
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
            return [i for i, n in enumerate(note_map) if self.key in n][0]
        except IndexError:
            raise NameError('The note is not indexed, try with enharmonics.')

    def diatonic_level(self):
        diatonic_grades = []
        for grade in self.scale_grades:
            note_index = (self.note_index() + grade)
            if note_index >= 12:
                note_index = note_index - 12
            diatonic_grades.append(note_index)
        return [x if x in diatonic_grades else '_' for x in self.chromatic_level]


abc = TPS('C', ['C', 'E', 'G'])
print(abc.diatonic_level())

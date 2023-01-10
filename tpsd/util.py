# pylint: disable=line-too-long
# pylint: disable=import-error
# pylint: disable=no-name-in-module
"""
This file contains utility functions to support the implementation of the Tonal
Pitch Step Distance (TPSD) algorithm
as presented in:

De Haas, W.B., Veltkamp, R.C., Wiering, F.: Tonal pitch step distance: a
similarity measure for chord progressions.
In: ISMIR. pp. 51–56 (2008)

Author: Andrea Poltronieri (University of Bologna) and Jacopo de Berardinis
(King's College of London)
Copyright: 2022 Andrea Poltronieri and Jacopo de Berardinis
License: MIT license
"""
import os

from biab import biab_chords


def open_harte(harte_file_path: str) -> (list[str], str):
    """
    Utility function that given a file containing chords notation encoded using
    the Harte notation, returns a list of
    the chords contained in the file
    :param harte_file_path: the path where the file is stored
    :return: a list of string, where each string corresponds to a chord.
    """
    with open(harte_file_path, 'r', encoding='utf-8') as harte_file:
        chords = [
            line.replace(
                '\n', ''
            ).replace(
                'hdim', 'hdim7'
            ).replace(
                '(s5,*5)', '1'
            ).replace(
                '*5', '1,3'
            ).replace(
                's9', '1,5,9'
            ).replace(
                's5',
                '1, 5')
            for line in
            harte_file]
    return chords[1:], chords[0]


def get_corresponding_biab(file_name: str, dataset_path: str) -> str:
    # pylint: disable=line-too-long
    """

    :param file_name:
    :param dataset_path:
    :return:
    """
    biab_file_name = \
        [file for file in os.listdir(dataset_path) if
         file == os.path.splitext(os.path.basename(file_name))[0]][0]
    return f'{dataset_path}/{biab_file_name}'


def parse_mgu(biab_path) -> list[int]:
    """
    Auxiliary function that takes as input the path of a Band-in-a-box file and
    returns a dictionary having as a key
    a chord and as a value the duration of such chord.
    Note that this piece of code only relies on the software implemented by
    Andrew Choi
    :param biab_path: tha path of the Band-in-a-box file
    :return: ???
    """
    biab = biab_chords(biab_path)
    return [int(stamp[1]) for stamp in biab]

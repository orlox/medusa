#!/usr/bin/env python
import sys
import os

__author__ = "Pablo Marchant"
__credits__ = ["Pablo Marchant", "Fabian Schneider"]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Pablo Marchant"
__email__ = "pamarca@gmail.com"

"""Module to read data from the NIST (National Institute for Standards and Technology).
"""

def read_nist_data(nist_data_filename):
    """Reads data from nist_data_filename, which contains isotope information.

    nist_data_filename: Filename for ascii file with isotope data. If file does
    not exist terminates the run.

    Returns a dictionary with relative atomic masses, with the keys being
    isotopes with their atomic numbers, i.e.

    {"h1": {"an":1, "mn":1, "am":1.00782503223},
     "h2": {"an":1, "mn":2, "am":2.01410177812},
     "he3":{"an":1, "mn":1, "am":3.0160293201}, etc...}

    """

    isotope_data = {}

    if not os.path.isfile(nist_data_filename):
        sys.exit("nist_data.py: Missing data file "+nist_data_filename)

    with open(nist_data_filename, 'r') as nist_file:

        atomic_number = -1
        atomic_symbol = ""
        mass_number = -1
        atomic_mass = 0e0

        for line in nist_file:
            if len(line) <= 1:
                continue

            entries = line.rstrip("\r\n").split(" = ")

            if entries[0] == "Atomic Number":
                atomic_number = int(entries[-1])
            elif entries[0] == "Atomic Symbol":
                atomic_symbol = entries[-1].lower()
            elif entries[0] == "Mass Number":
                mass_number = int(entries[-1])
                if atomic_number == 1:
                    atomic_symbol = "h"+str(mass_number)
                else:
                    atomic_symbol = atomic_symbol+str(mass_number)
            elif entries[0] == "Relative Atomic Mass":
                atomic_mass = float(entries[-1].split("(")[0])
                isotope_data[atomic_symbol] = \
                        {"an":atomic_number, "mn":mass_number, "am":atomic_mass}

        return isotope_data


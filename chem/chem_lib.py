#!/usr/bin/env python
import sys
import yaml
import os

from medusa.chem.private import nist_data
from medusa.const import const_lib

__author__ = "Pablo Marchant"
__credits__ = ["Pablo Marchant", "Fabian Schneider"]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Pablo Marchant"
__email__ = "pamarca@gmail.com"

"""Module to initialize composition information.
Much of this is copied from the MESA code.
Used to read files specifying element abundance or mass fractions.
"""

#read out isotope information
ISOTOPE_DATA = nist_data.read_nist_data(os.environ["MEDUSA_DIR"]+"/chem/data/isotope.data")

def get_chem_data(chem_filename, has_mass_fractions=False):
    """Reads data from chem_filename, which contains composition information
    in either abundance (A=12+log(nA/nh) where nA and nh are number densities of
    elements A and hydrogen), or mass fractions. Returns a dictionary containing
    abundances

    chem_filename: Name of a yaml configuration file containing abundance
    information. The file is looked first at the current directory, and in
    case it does not exist, is looked in $MEDUSA_PATH/chem/data. If file
    is not found, it terminates the program.

    has_mass_fractions: True if input file has.

    """

    # Check for the existance of chem_filename. If file is missing,

    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

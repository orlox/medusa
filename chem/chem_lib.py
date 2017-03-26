#!/usr/bin/env python
import sys
import yaml
import os
import numpy as np

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

def get_chem_data(chem_filename):
    """Reads data from chem_filename, which contains composition information
    in either abundance (A=12+log(nA/nh) where nA and nh are number densities of
    elements A and hydrogen), or mass fractions. Returns a dictionary containing
    abundances and relative metal mass fractions.

    chem_filename: Name of a yaml configuration file containing abundance
    information. The file is looked first at the current directory, and in
    case it does not exist, is looked in $MEDUSA_PATH/chem/data. If file
    is not found, it terminates the program. Yaml file should contain


    """

    chem_data = {}

    if not os.path.isfile(chem_filename):
        if not os.path.isfile(os.environ['MEDUSA_DIR']+"/chem/data/"+chem_filename):
            sys.exit("chem_lib.py: Missing data file "+chem_filename+" in get_chem_data")
        chem_filename = os.environ['MEDUSA_DIR']+"/chem/data/"+chem_filename

    with open(chem_filename, 'r') as ymlfile:
        chem_data = yaml.load(ymlfile)

    #validate yaml file and compute/normalize metal fractions if needed
    sum_z = 0
    if "abundances" in chem_data.keys():
        if "mass_fractions" in chem_data.keys():
            sys.exit("chem_lib.py: input file contains both 'abundances' and 'mass_fractions'")

        chem_data["mass_fractions"] = {}
        for key in chem_data["abundances"].keys():
            if key not in ISOTOPE_DATA.keys():
                sys.exit("chem_lib.py: Invalid entry "+key+" in input file")
            chem_data["mass_fractions"][key] = \
                    np.power(10,chem_data["abundances"][key])*ISOTOPE_DATA[key]["am"]
            sum_z += chem_data["mass_fractions"][key]
        for key in chem_data["abundances"].keys():
            chem_data["mass_fractions"][key] /= sum_z

    elif "mass_fractions" in chem_data.keys():
        for key in chem_data["abundances"].keys():
            if key not in ISOTOPE_DATA.keys():
                sys.exit("chem_lib.py: Invalid entry "+key+" in input file")
            sum_z += chem_data["mass_fractions"][key]
        for key in chem_data["abundances"].keys():
            chem_data["mass_fractions"][key] /= sum_z

    else:
        sys.exit("chem_lib.py: Missing either 'abundances' or 'mass_fractions' in input file")

    return chem_data


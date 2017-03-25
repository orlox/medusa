#!/usr/bin/env python
import sys
import yaml
import os

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

ELEMENT_NAMES = [
        'neut','h','he','li','be','b','c','n','o','f','ne',
        'na','mg','al','si','p','s','cl','ar','k','ca',
        'sc','ti','v','cr','mn','fe','co','ni','cu','zn',
        'ga','ge','as','se','br','kr','rb','sr','y','zr',
        'nb','mo','tc','ru','rh','pd','ag','cd','in','sn',
        'sb','te','i','xe','cs','ba','la','ce','pr','nd',
        'pm','sm','eu','gd','tb','dy','ho','er','tm','yb',
        'lu','hf','ta','w','re','os','ir','pt','au','hg',
        'tl','pb','bi','po','at','rn','fr','ra','ac','th',
        'pa','u','np','pu','am','cm','bk','cf','es','fm','md',
        'no','lr','rf','db','sg','bh','hs','mt','ds','rg','cn'
        ]

ELEMENT_ATOMIC_WEIGHTS = {
         #periodic table, row 1
         "h" : 1.00794
         "he" : 4.002602

         #periodic table, row 2
         "li" = 6.941
         "be" = 9.012
         "b"  = 10.811
         "c"  = 12.0107
         "n"  = 14.0067
         "o"  = 15.9994
         "f"  = 18.9984032
         "ne" = 20.1797

         #periodic table, row 3
         "na" = 22.989770
         "mg" = 24.3050
         "al" = 26.981538
         "si" = 28.0855
         "p"  = 30.973761
         "s"  = 32.065
         "cl" = 35.453
         "ar" = 39.948

         #periodic table, row 4
         "k"  = 39.0983
         "ca" = 40.078
         "sc" = 44.955910
         "ti" = 47.867
         "v"  = 50.9415
         "cr" = 51.9961
         "mn" = 54.938049
         "fe" = 55.845
         "co" = 58.933200
         "ni" = 58.6934
         "cu" = 63.546
         "zn" = 65.409
         "ga" = 69.723
         "ge" = 72.64
         "as" = 74.921
         "se" = 78.96
         "br" = 79.904
         "kr" = 83.798

         #periodic table, row 5
         element_atomic_weight(e_rb) = 85.4678
         element_atomic_weight(e_sr) = 87.62
         element_atomic_weight(e_y) =  88.905
         element_atomic_weight(e_zr) = 91.224
         element_atomic_weight(e_nb) = 92.906
         element_atomic_weight(e_mo) = 95.94
         element_atomic_weight(e_tc) = 97.9072
         element_atomic_weight(e_ru) = 101.07
         element_atomic_weight(e_rh) = 102.905
         element_atomic_weight(e_pd) = 106.42
         element_atomic_weight(e_ag) = 107.8682
         element_atomic_weight(e_cd) = 112.411
         element_atomic_weight(e_in) = 114.818
         element_atomic_weight(e_sn) = 118.710
         element_atomic_weight(e_sb) = 121.760
         element_atomic_weight(e_te) = 127.60
         element_atomic_weight(e_i ) = 126.904
         element_atomic_weight(e_xe) = 131.293

         #periodic table, row 6
         element_atomic_weight(e_cs) = 132.905
         element_atomic_weight(e_ba) = 137.327
         element_atomic_weight(e_la) = 138.9055
         element_atomic_weight(e_ce) = 140.115
         element_atomic_weight(e_pr) = 140.90765
         element_atomic_weight(e_nd) = 144.24
         element_atomic_weight(e_pm) = 144.9127
         element_atomic_weight(e_sm) = 150.36
         element_atomic_weight(e_eu) = 151.965
         element_atomic_weight(e_gd) = 157.25
         element_atomic_weight(e_tb) = 158.92534
         element_atomic_weight(e_dy) = 162.50
         element_atomic_weight(e_ho) = 164.93032
         element_atomic_weight(e_er) = 167.26
         element_atomic_weight(e_tm) = 168.93421
         element_atomic_weight(e_yb) = 173.04
         element_atomic_weight(e_lu) = 174.967
         element_atomic_weight(e_hf) = 178.49
         element_atomic_weight(e_ta) = 180.9479
         element_atomic_weight(e_w ) = 183.84
         element_atomic_weight(e_re) = 186.207
         element_atomic_weight(e_os) = 190.23
         element_atomic_weight(e_ir) = 192.22
         element_atomic_weight(e_pt) = 195.08
         element_atomic_weight(e_au) = 196.96654
         element_atomic_weight(e_hg) = 200.59
         element_atomic_weight(e_tl) = 204.3833
         element_atomic_weight(e_pb) = 207.2
         element_atomic_weight(e_bi) = 208.98037
         element_atomic_weight(e_po) = 208.9824
         element_atomic_weight(e_at) = 209.9871
         element_atomic_weight(e_th) = 232.0381
         element_atomic_weight(e_pa) = 231.03588
         element_atomic_weight(e_u)  = 238.02891

        }

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

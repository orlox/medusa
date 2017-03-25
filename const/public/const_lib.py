#!/usr/bin/env python
import math
"""Define multiple constants. Much of this taken directly from MESA.

This module simply defines a multitude of constants for general use.
Importing this module as

from const_lib import *

will allow access to multiple useful constants such as PI and RSUN.

TODO: Potentially better to use scipy.constants and convert units
"""

PI = math.pi
EULERCON = math.e
CGRAV = 6.67428e-8                 # gravitational constant (g^-1 cm^3 s^-2)
PLANCK_H = 6.62606896e-27          # Planck's constant (erg s)
HBAR = PLANCK_H / (2*PI)
QE = 4.80320440e-10                # electron charge (esu == (g cm^3 s^-2)^(1/2))
AVO = 6.02214179e23                # Avogadro's constant (mole^-1)
CLIGHT = 2.99792458e10             # speed of light in vacuum (cm s^-1)
KERG = 1.3806504e-16               # Boltzmann's constant (erg K^-1)
CGAS = KERG*AVO                    # ideal gas constant; erg/K
KEV = 8.617385e-5                  # converts temp to ev (ev K^-1)
AMU = 1.660538782e-24              # atomic mass unit (g)

MN = 1.6749286e-24                 # neutron mass (g)
MP = 1.6726231e-24                 # proton mass (g)
ME = 9.1093826e-28                 # (was 9.1093897d-28) electron mass (g)
RBOHR = HBAR**2/(ME * QE**2)       # Bohr radius (cm)
FINE = QE**2/(HBAR*CLIGHT)         # fine structure constant
HION = 13.605698140e0              # hydrogen ionization energy (eV)
EV2ERG = 1.602176487e-12           # electron volt (erg)
MEV_TO_ERGS = 1e6*EV2ERG
MEV_AMU = MEV_TO_ERGS/AMU
QCONV = MEV_TO_ERGS*AVO

BOLTZ_SIGMA = 5.670400e-5          # boltzmann's sigma = a*c/4 (erg cm^-2 K^-4 s^-1)
CRAD = BOLTZ_SIGMA*4/CLIGHT        # = radiation density constant, a (erg cm^-3 K^-4); Prad = crad * T^4 / 3
                                   # approx = 7.5657e-15

WEINLAM = PLANCK_H*CLIGHT/(KERG * 4.965114232e0)
WEINFRE = 2.821439372E0*KERG/PLANCK_H
RHONUC = 2.342e14                  # density of nucleus (g cm^3)

# solar age, L, and R values from Bahcall et al, ApJ 618 (2005) 1049-1056.
MSUN = 1.9892e33                   # solar mass (g)  <<< gravitational mass, not baryonic
RSUN = 6.9598e10                   # solar radius (cm)
LSUN = 3.8418e33                   # solar luminosity (erg s^-1)
AGESUN = 4.57e9                    # solar age (years)
LY = 9.460528e17                   # light year (cm)
PC = 3.261633e0*LY                 # parsec (cm)
SECYER = 3.1558149984e7            # seconds per year
DAYYER = 365.25e0                  # days per year

TEFFSOL = 5777.0e0
LOGGSOL = 4.4378893534131256e0     # With mesa's default msol, rsol and standard_cgrav
MBOLSUN = 4.746                    # Bolometric magnitude of the Sun
M_EARTH = 5.9764e27                # earth mass (g)
                                   # = 3.004424e-6 Msun
R_EARTH = 6.37e8                   # earth radius (cm)
AU = 1.495978921e13                # astronomical unit (cm)
M_JUPITER = 1.8986e30              # jupiter mass (g)
                                   # = 0.954454d-3 Msun
R_JUPITER = 6.9911e9               # jupiter mean radius (cm)
SEMIMAJOR_AXIS_JUPITER = 7.7857e13 # jupiter semimajor axis (cm)


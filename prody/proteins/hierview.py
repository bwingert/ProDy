# ProDy: A Python Package for Protein Structural Dynamics Analysis
# 
# Copyright (C) 2010  Ahmet Bakan <ahb12@pitt.edu>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

""":mod:`hierview` module defines a class for a hieararchical view of an atom 
group and atom selections

Classes:
    
  * :class:`HierView`

"""

__author__ = 'Ahmet Bakan'
__copyright__ = 'Copyright (C) 2010  Ahmet Bakan'

from collections import defaultdict

import numpy as np

import prody
from prody import ProDyLogger as LOGGER
from . import Chain, Residue, Selection, DTYPES


__all__ = ['HierView']



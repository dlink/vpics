#!/usr/bin/env python

import os
import sys

# add vpics lib to PYTHONPATH:
libdir = os.path.dirname(os.path.realpath(__file__)).replace('/web', '/lib')
sys.path.append(libdir)

from collection import Collection
Collection().go()

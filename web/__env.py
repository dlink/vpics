#!/usr/bin/env python

import os

from vweb.htmltable import HtmlTable

print 'Content-Type: text/html\n'

table = HtmlTable()

keys = os.environ.keys()
for k in sorted(keys):
    table.addRow([k, os.environ[k]])

print table.getTable()


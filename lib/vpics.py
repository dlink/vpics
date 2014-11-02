#!/usr/bin/env python 

import sys
import os
import copy
#from datetime import datetime

#import vlib.conf as conf
#import vlib.logger as logger

VERBOSE = 0

class VPics(object):

    def __init__(self):
        self.verbose = VERBOSE 
        #self.logger = logger.getLogger(self.__class__.__name__)

    def process(self, *args):

        # get verbose flag
        if args and args[0] == '-v':
            self.verbose = 1
            args = args[1:]

        if not args:
            syntax()

        
def syntax(emsg=None):
    prog = os.path.basename(sys.argv[0])
    if emsg:
        print emsg
    ws = ' '*len(prog)

    print
    print "   %s hi" % prog
    print
    sys.exit(1)

if __name__ == '__main__':
    args = copy.copy(sys.argv[1:])
    verbose = args and args[0] == '-v'

    retcode = 0
    try:
        results = VPics().process(*args)
    except Exception, e:
        if verbose: 
            raise
        results = "Failed: %s: %s" % (e.__class__.__name__, str(e))
        retcode = 100

    print results
    sys.exit(retcode)

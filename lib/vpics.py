#!/usr/bin/env python 

import sys
import os
import copy
#from datetime import datetime

#import vlib.conf as conf
#import vlib.logger as logger

from data import Data
import data

VERBOSE = 0

CONF_NAME = 'vpics.conf'

class VPicsError(Exception): pass

class VPics(object):

    def __init__(self):
        self.verbose = VERBOSE 
        #self.logger = logger.getLogger(self.__class__.__name__)

    def process(self, *args):

        # get verbose flag
        if args and args[0] == '-v':
            self.verbose = 1
            args = args[1:]

        if len(args) < 2:
            syntax()

        cmd = args[0]
        subdir = args[1].rstrip('/')

        if cmd != 'update':
            raise VPicsError('Unrecognized Command: %s' % cmd)
        
        # validate subdir
        if not os.path.isdir(subdir):
            raise VPicsError('%s is not a subdirectlry' % subdir)

        # set config file:
        filename = "%s/%s" % (subdir, CONF_NAME)
        print 'filename:', filename
        if not os.path.isfile(filename):
            data.createConfigFile(filename)
        self.data = Data(filename)
        return self.data
        
def syntax(emsg=None):
    prog = os.path.basename(sys.argv[0])
    if emsg:
        print emsg
    ws = ' '*len(prog)

    print
    print "   %s update <subdir>" % prog
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

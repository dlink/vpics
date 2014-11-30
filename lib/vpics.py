#!/usr/bin/env python 

import sys
import os
import copy

from vlib.odict import odict
#from datetime import datetime

#import vlib.conf as conf
#import vlib.logger as logger

#from data import Data
#import data

VERBOSE = 0

CONF_NAME = 'vpics.yaml'

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
        if 0: #os.path.isfile(filename):
            print "File '%s' exists." % filename
        else:
            print "Creating file '%s'" % filename
            data = self.createConfig(subdir)
            open(filename, 'w').write(self.formatConfig(data))
        #self.data = data.getInstance()
        return 'Done'
        
    def createConfig(self, subdir):
        data = odict(pages=[])
        warnings = []

        # get pages from subdirectories
        for file in os.listdir(subdir):

            if file == CONF_NAME:
                continue

            if os.path.isdir("%s/%s" % (subdir, file)):
                data.pages.append(file)
            else:
                warnings.append('Unrecognized file: "%s" is not a directory'
                                % file)

        # get images and phtml files for each page
        for page in data.pages:
            data[page] = odict(pics=[], html={})
            for file in os.listdir("%s/%s" % (subdir, page)):
                ext = file.split('.')[-1]

                # html pages:
                if ext == 'phtml':
                    if 'filename' in data[page].html:
                        warnings.append('Page "%s" already has a phtml file: '
                                        '"%s".  Skipping "%s"'
                                        % (page, data[page].html.filename,
                                           file))

                    data[page].html = odict(filename=file)
                elif ext == 'jpg':
                    pic = odict(name=file.replace('.'+ext, ''),
                                filename=file,
                                caption='',
                                description='')
                    data[page].pics.append(pic)
                else:
                    warnings.append('Unrecognized file extention: "%s".  '
                                    'File: "%s/%s/%s"'
                                    % (ext, subdir,  page, file))
        if warnings:
            print 'Warnings:'
            print '\n'.join(["%s. %s" %(i+1,j) for i,j in enumerate(warnings)])
        return data

    def formatConfig(self, data):
        ind = '   '

        o = ''
        o += 'pages:\n'
        for page in data.pages:
            o += '%s- %s\n' % (ind, page)
        o += '\n'
        for page in data.pages:
            o += '%s:\n' % page
            if 'filename' in data[page].html:
                o += '%shtml:\n' % ind
                o += '%sfilename: %s\n' % (ind*2, data[page].html.filename)
            if data[page].pics:
                o += '%spics:\n' % ind
                for pic in data[page].pics:
                    o += '%s- name       : %s\n' % (ind*2, pic.name)
                    o += '%s  filename   : %s\n' % (ind*2, pic.filename)
                    o += '%s  caption    : %s\n' % (ind*2, pic.caption)
                    o += '%s  description: %s\n' % (ind*2, pic.description)
                    o += '\n'
        print o.strip()
        return o


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

#!/usr/bin/env python 

import sys
import os
import copy

from vlib.odict import odict

VERBOSE = 0

CONF_NAME = 'vpics.yaml'
THUMBNAILS = '200px'

class VPicsError(Exception): pass

class VPics(object):

    def __init__(self):
        self.verbose = VERBOSE 

    def process(self, *args):

        # get verbose flag
        if args and args[0] == '-v':
            self.verbose = 1
            args = args[1:]

        if len(args) < 2:
            syntax()

        cmd = args[0]
        subdir = args[1].rstrip('/')

        if cmd == 'update':
            return self.update(subdir)
        else:
            raise VPicsError('Unrecognized Command: %s' % cmd)
        
    def update(self, subdir):
        # validate subdir
        if not os.path.isdir(subdir):
            raise VPicsError('%s is not a subdirectlry' % subdir)

        # set config file:
        filename = "%s/%s" % (subdir, CONF_NAME)
        if 0: #os.path.isfile(filename):
            print "File '%s' exists." % filename
        else:
            data, warnings = self._gatherMetadata(subdir)
            if warnings:
                print 'Warnings:'
                print '\n'.join(["  %s. %s" %(i+1,j)
                                 for i,j in enumerate(warnings)])
                print
            # write config
            open(filename, 'w').write(self._formatConfig(data))
            print 'Config file: %s written.' % filename
        return 'Done.'
        #self.data = data.getInstance()
        
    def _gatherMetadata(self, subdir):
        '''Given the name of a media subdirectory
           Return a data dictionary media's metadata, and
                  a warning list
        '''
        SKIPPERS = ['200px', 'vpics.yaml']

        # default site_name to subdirname
        site_name = subdir.split('/')[-1].replace('_', ' ').title()

        data = odict(site_name    = site_name,
                     site_message = '',
                     media_url    = 'NEED_TO_SET_THIS_IN_vpics.yaml',
                     pages        = [])

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
            page_dir      = "%s/%s"    % (subdir, page)
            thumbnail_dir = "%s/%s/%s" % (subdir, page, THUMBNAILS)

            data[page] = odict(pics=[], html={})
            for file in os.listdir(page_dir):
                if file in SKIPPERS:
                    continue
                ext = file.split('.')[-1]

                # html pages:
                if ext == 'phtml':
                    if 'filename' in data[page].html:
                        warnings.append('Page "%s" already has a phtml file: '
                                        '"%s".  Skipping "%s"'
                                        % (page, data[page].html.filename,
                                           file))

                    data[page].html = odict(filename=file)

                # Pictures
                elif ext == 'jpg':
                    pic = odict(name=file.replace('.'+ext, ''),
                                filename=file,
                                caption='',
                                description='')
                    data[page].pics.append(pic)

                # Unknowns
                else:
                    warnings.append('Unrecognized file extention: "%s".  '
                                    'File: "%s/%s/%s"'
                                    % (ext, subdir,  page, file))

            # look for thumbnail dir
            if data[page].pics and not os.path.exists(thumbnail_dir):
                warnings.append('Thumbnail directory for page "%s" '
                                'not found: %s' % (page, thumbnail_dir))

        return data, warnings

    def _formatConfig(self, data):
        ind = '   '

        o = ''
        o += 'site_name: %s\n\n'    % data.site_name
        o += 'site_message: %s\n\n' % data.site_message
        o += 'media_url: %s\n\n'    % data.media_url
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

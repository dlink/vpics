#!/usr/bin/env python 

import sys
import os
import copy
import shutil
from datetime import datetime

from vlib.odict import odict

VERBOSE = 0

CONF_NAME = 'vpics.yaml'
THUMBNAILS = '200px'

class VPicsError(Exception): pass

class VPics(object):
    '''Preside over the Vpics system'''

    def __init__(self):
        self.verbose = VERBOSE 

    def process(self, *args):
        '''Process incoming requests'''

        # get verbose flag
        if args and args[0] == '-v':
            self.verbose = 1
            args = args[1:]

        # get yes flag
        overwrite = 0
        if '-y' in args:
            overwrite = 1
            p = args.index('-y')
            args = args[0:p]+args[p+1:]

        if len(args) < 2:
            syntax()

        cmd = args[0]
        subdir = args[1].rstrip('/')

        if cmd == 'update':
            return self.update(subdir, overwrite=overwrite)
        else:
            raise VPicsError('Unrecognized Command: %s' % cmd)
        
    def update(self, subdir, overwrite=False):
        '''Given a subdirectory
           Create or update the vpics.yml file

           if overwrite is true, then don't ask about overwriting
           existing vpics.yml file
        '''
        # validate subdir
        if not os.path.isdir(subdir):
            raise VPicsError('%s is not a subdirectory' % subdir)

        # set config file:
        filename = "%s/%s" % (subdir, CONF_NAME)

        # does a config already exist - if so read it's data
        data1 = None
        if os.path.isfile(filename):
            print "Config file: %s already exists.  A backup will be made." \
                % filename
            if not overwrite:
                are_you_sure('Update existing file?')
            data1 = self._getExistingData(filename)

        # gather meta data from subdir, and existing data
        data, warnings = self._gatherMetadata(subdir, data1)
        if warnings:
            print 'Warnings:'
            print '\n'.join(["  %s. %s" %(i+1,j)
                             for i,j in enumerate(warnings)])
            print

        # backup existing file if nec.
        if data1:
            timestamp = str(datetime.now()).replace(' ', '::')[0:20]
            bk_filename = '%s_%s' % (filename, timestamp)
            shutil.copyfile(filename, bk_filename)
            print 'Existing config file moved to: %s' % bk_filename

        # write config
        open(filename, 'w').write(self._formatConfig(data))

        print 'New config file: %s written.' % filename
        return 'Done.'
        
    def _getExistingData(self, filename):
        from data import Data
        return Data(filename).data

    def _gatherMetadata(self, subdir, data):
        '''Given the name of a media subdirectory
           Return a data dictionary media's metadata, and
                  a warning list
        '''
        SKIPPERS = ['200px', 'vpics.yaml']

        # init
        warnings = []
        if not data:
            # default site_name to subdirname
            site_name = subdir.split('/')[-1].replace('_', ' ').title()
            data = odict(site_name    = site_name,
                         site_message = '',
                         media_url    = 'NEED_TO_SET_THIS_IN_vpics.yaml',
                         pages        = [])

        # get pages from subdirectories
        for file in os.listdir(subdir):
            if file.startswith(CONF_NAME):
                continue

            # append pages to data if nec.:
            if os.path.isdir("%s/%s" % (subdir, file)):
                if file not in data.pages:
                    data.pages.append(file)
            else:
                warnings.append('Unrecognized file: "%s" is not a directory'
                                % file)

        # get images and phtml files for each page
        for page in data.pages:

            # init
            page_dir      = "%s/%s"    % (subdir, page)
            thumbnail_dir = "%s/%s/%s" % (subdir, page, THUMBNAILS)
            page_filenames = []
            if page in data:
                page_filenames = [x['filename'] for x in data[page]['pics']]
            if page not in data:
                data[page] = odict(pics=[], html={})

            # loop thru subdirectory files in reverse order and prepend them
            # This allows
            #   1. inital alphabetical listing
            #   2. newest files to the top when added

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
                elif ext in ('png', 'jpg', 'jpeg'):
                    if file not in page_filenames:
                        pic = odict(name=file.replace('.'+ext, ''),
                                    filename=file,
                                    caption='',
                                    description='')
                        data[page].pics.insert(0, pic)

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
            if data[page].html and 'filename' in data[page].html:
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

def are_you_sure(question):
    '''Ask given question
       provide prompt (y/N)
       read import Default to 'No'
       exit on 'No'
    '''
    print "%s (y/N): " % question,
    yn = sys.stdin.readline()
    yn = yn.strip()
    print
    if yn.upper() != 'Y':
        print 'No action taken.'
        sys.exit(1)

def syntax(emsg=None):
    prog = os.path.basename(sys.argv[0])
    if emsg:
        print emsg
    ws = ' '*len(prog)

    print
    print "   %s [OPTIONS] update <subdir>" % prog
    print
    print "   %s OPTIONS: -v verbose" % ws
    print "   %s          -y Answer Yes to Update existing file" % ws
    print
    sys.exit(1)

if __name__ == '__main__':
    args = copy.copy(sys.argv[1:])

    # verbose?
    verbose = 0
    if '-v' in args:
        verbose = 1
        p = args.index('-v')
        args = args[0:p]+args[p+1:]

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

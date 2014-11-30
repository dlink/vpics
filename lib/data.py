#!/usr/bin/env python

import os
import yaml

from vlib.odict import odict

CONF_ENV_VAR = 'VCONF'

class DataError(Exception): pass

class Data(object):
    '''
Input YAML structure:
---------------------
   site_name: Artworks

   site_message: <p>Message to users here</p>

   media_url: art-images

   pages:
      - Sculptures
      - Paintings

   Sculptures:
      pics:
         - filename: Sinner.jpg
         - filename: Angel.jpg

   Paintings:
      pics:
         - filename: Tasteless.jpg
         - filename: Budddha_watercolor.jpg
   About:
      html:
        filename: about.html
'''


    def __init__(self):
        try:
            self.filename = os.environ[CONF_ENV_VAR]
        except KeyError, e:
            raise DataError('Environment variable %s not defined.'
                            % CONF_ENV_VAR)
        try:
            self.data = odict(yaml.load(open(self.filename, 'r')))
        except Exception, e:
            raise DataError('Unable to parse yaml: %s\n%s: %s'
                            % (self.filename, e.__class__.__name__, e))

        self.data.config_filename = self.filename
        self._validateData()
        self._consolidateAndSetDefaultsPics()

    def _validateData(self):
        filename = self.filename

        # check these attributes:
        attributes = ['site_name', 'site_message', 'media_url', 'pages']
        for a in attributes:
            if a not in self.data:
                raise DataError("%s: '%s' not found" % (filename, a))

        # each page has entry
        for page_name in self.data.pages:
            if page_name not in self.data:
                raise DataError("%s: page definition for '%s' not found."
                                % (filename, page_name))
            #if 'pic' in self.data[page_name]:
            #    self.data[page_name].pic = odict(self.data[page_name].pic)

    def _consolidateAndSetDefaultsPics(self):
        '''Gather all Pics defined in all Pages into data.pics
           Add defaults for name, caption, and description
        '''
        data = self.data

        # init a collection of all pics
        data.pics = odict()

        # Loop thru each page
        for page_name in data.pages:

            # convert data[page_name] to odict
            data[page_name] = odict(data[page_name])

            # does page have html?
            if 'html' in data[page_name]:
                data[page_name].html = odict(data[page_name].html)
            else:
                data[page_name].html = None

            # does page have pics:
            if 'pics' not in data[page_name]:
                data[page_name].pics = []
                continue

            # make pics a list of odicts rather than of dics:
            for i, pic in enumerate(data[page_name].pics):
                data[page_name].pics[i] = odict(pic)

            # add annotated fields, and consolidate into data.pics
            for i, pic in enumerate(data[page_name].pics):
                if 'name' not in pic:
                    pic.name = pic['filename'].split('.')[0]
                if 'caption' not in pic:
                    pic.caption = ''
                if 'description' not in pic:
                    pic.description = ''
                pic.page_name = page_name

                data.pics[pic.name] = pic

__data = Data().data
def getInstance():
    '''Return a single instance of Data()'s data property'''
    return __data

if __name__ == '__main__':
    from pprint import pprint

    data = getInstance()
    print 'Data Dump:'
    print pprint(data)

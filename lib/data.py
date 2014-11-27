#!/usr/bin/env python

import yaml

from vlib.odict import odict

#FILENAME = '/data/vpics-images/vpics.conf'
FILENAME = '/data/dev-vpics/vpics.yaml'

class DataError(Exception): pass

class Data(object):
    '''
Input YAML structure:
---------------------
   pages:
      - Sculptures
      - Paintings
 
   Sculptures:
      - pics:
         - filename: Sinner.jpg
         - filename: Angel.jpg

   Paintings:
      - pics:
         - filename: Tasteless.jpg
         - filename: Budddha_watercolor.jpg 
   About:
      - html:
        - filename: about.html
'''


    def __init__(self, filename=FILENAME):
        # TODO : default fiename to ENV

        self.filename = filename
        self.data = odict(yaml.load(open(filename, 'r')))

        self._validateData()
        self._consolidatePics()

    def _validateData(self):
        filename = self.filename

        # has pages key:
        if 'pages' not in self.data:
            raise DataError("%s: 'pages' not found" % filename)

        # each page has entry
        for page_name in self.data.pages:
            if page_name not in self.data:
                raise DataError("%s: page definition for '%s' not found." 
                                % (filename, page_name))
    def _consolidatePics(self):
        '''Gather all Pics defined in all Pages'''
        self.data.pics = odict()
        for page_name in self.data.pages:
            if 'pics' not in self.data[page_name]:
                continue
            for pic in self.data[page_name]['pics']:
                pic = odict(pic)
                self.data.pics[pic.filename] = pic

__data = Data().data
def getInstance():
    '''Return a single instance of Data()'s data property
    '''
    return __data

if __name__ == '__main__':
    from pprint import pprint
    data = getInstance()
    print 'Data Dump:'
    print pprint(data)

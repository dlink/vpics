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
        self._consolidateAndSetDefaultsPics()

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
            #if 'pic' in self.data[page_name]:
            #    self.data[page_name].pic = odict(self.data[page_name].pic)

    def _consolidateAndSetDefaultsPics(self):
        '''Gather all Pics defined in all Pages into data.pics
           Add defaults for name, caption, and description
        '''
        data = self.data

        data.pics = odict()
        for page_name in data.pages:
            if 'pics' not in data[page_name]:
                continue

            # convert to odict
            data[page_name] = odict(data[page_name])

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
                data.pics[pic.filename] = pic

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

#!/usr/bin/env python

import yaml

from vlib.odict import odict

FILENAME = '/data/vpics-images/vpics.conf'

class DataException(Exception): pass

class Data(object):
    '''
Input YAML structure:
---------------------
   pages:
      - Sculptures
      - Paintings
 
   Sculptures:
      - filename: Sinner.jpg
      - filename: Angel.jpg

   Paintings:
      - filename: Tasteless.jpg
      - filename: Budddha_watercolor.jpg 


Internal Representation
-----------------------
   pages:
      Sculpture:
         id: 1
         name: Sculpture
         pics:
            - odict( .. pic Sinner ..)
            - odict( .. pic Angel ..)
      Painting:
         id: 2
         name: Painting
         pics:
            - odict( .. Tasteless ..)
            - odict( .. Buddha_watercolor ..)
   Pics:
      Sinner:
         id: 1
         name: Sinner
         filename: Sinner.jpg
         page_name: Sculpture
      Angel:
         id: 2
         name: Angel
         filename: Angel.jpg
         page_name: Sculpture
      ...

        '''

    def __init__(self):
        # Read yaml data:
        self.yaml_data = odict(yaml.load(open(FILENAME, 'r')))

        # Build internal data (odicts)
        self.data = odict(pages=odict(), pics =odict())
        for page_id, page_name in enumerate(self.yaml_data.pages, start=1):
            for pic_id, pic in enumerate(self.yaml_data[page_name], start=1):
                pic = odict(pic)

                # pic must have filename
                if 'filename' not in pic:
                    raise DataException('pic does not contain filename: %s' 
                                        % pic)

                # init pic odict data
                if 'name' not in pic:
                    pic.name = pic['filename'].split('.')[0]
                if 'caption' not in pic:
                    pic.caption = ''
                if 'description' not in pic:
                    pic.description = ''
                pic.id = pic_id
                pic.page_name = page_name


                # store pic under pics:
                self.data.pics[pic.name] = pic

                # store pic under pages
                if page_name not in self.data.pages:
                    self.data.pages[page_name] = odict(id=page_id,
                                                       name=page_name,
                                                       pics=[])
                self.data.pages[page_name].pics.append(pic)

    
    def dump(self):
        '''Return a nicely formated data dump of internal data
           suitable for printing
        '''
        o = ''
        for key1, value1 in data.data.items():
            o += "%s:\n" % key1
            for key2, value2 in value1.items():
                o += "   %s:\n" % key2
                for key3, value3 in value2.items():
                    display = value3
                    if key3 == 'pics':
                        display = '; '.join([x['name'] for x in value3])
                    o += "      %s: %s\n" % (key3, display)
            o += '\n'
        return o


if __name__ == '__main__':
    from vlib.utils import pretty

    # display data:
    data = Data()
    print 'Yaml Data:'
    print pretty(data.yaml_data)
    print
    print 'Internal Data:'
    print data.dump()

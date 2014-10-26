#!/usr/bin/env python

import yaml

from vlib.odict import odict

FILENAME = '/data/vpics-images/vpics.conf'

class DataException(Exception): pass

class Data(object):

    def __init__(self):
        '''Input YAML structure:
           ---------------------
           pages          - list of page_names as STR
           Each page_name - a list of pics as DICT

              pages:
                 - Sculptures
            
              Sculptures:
                 - filename: Sinner.jpg
             
                 - filename: Angel.jpg


           Internal Representation
           pages - a collection of pages as DICTs
                   maintains numerical Id for ordering

           Each Page - a collection of pics as DICTs
                       maintians numerical Id for ordering within Page

           pics - a collection of pics as DICTs (redundunt with 'Each Page')
                  maintains numerical id for ordering accross all pics
                  maintains 'page' to know which page it belongs to.

              pages:
                 Sculpture:
                    id: 1
                    name: Sulpture

              Sculpture:
                 Sinner:
                    id: 1
                    name: Sinner
                    filename: Sinner.jpg
                 Angel:
                    id: 2
                    name: Angel
                    filename: Angel.jpg

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

        '''
        # read yaml data:
        self.yaml_data = odict(yaml.load(open(FILENAME, 'r')))

        # init internal data:
        self.data = odict(pages=odict(), pics =odict())

        # build internal data:
        for page_name in self.yaml_data.pages:
            for id, pic in enumerate(self.yaml_data[page_name]):
                pic = odict(pic)

                # pic must have filename
                if 'filename' not in pic:
                    raise DataException('pic does not contain filename: %s' 
                                        % pic)

                # default pic name, if nec,  to filename minus extention
                if 'name' not in pic:
                    pic.name = pic['filename'].split('.')[0]
                    
                # add id:
                pic.id = id

                # add page_name
                pic.page_name = page_name

                # store pic under pics:
                self.data.pics[pic.name] = pic

                # store pic under pages:
                if page_name not in self.data.pages:
                    self.data.pages[page_name] = odict()
                self.data.pages[page_name][pic.name] = pic

        #self.data
        #for page_name in self.data.pages:
        #    print 'page_name:', page_name
        #    for pic in self.data[page_name]:
        #        print 'pic:', pic
        #        self.data.pics.append(pic)

if __name__ == '__main__':
    from vlib.utils import pretty

    data = Data()
    print pretty(data.yaml_data)
    print
    print pretty(data.data)

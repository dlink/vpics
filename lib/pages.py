#from data import Data
import data
from pics import Pic

class Pages(object):
    '''Preside over Pages Data
    '''

    def __init__(self):
        #self.data = Data().data.pages
        self.data = data.getInstance().pages
        
    def getAll(self):
        '''Return a list of Page Objects
        '''
        return self.data

    @property
    def first_page(self):
        '''Return and instantiated Page that has the lowest id'''
        min_page_id = None
        page_name = None
        for page_name, data in self.data.items():
            if not min_page_id or data.id < min_page_id:
                min_page_id = data.id
                name = data.name
        return Page(page_name)
    @property
    def list(self):
        '''Return a list of instantiated Page objects in id order'''
        page_ids = {}
        for page_name, data in self.data.items():
            page_ids[data.id] = Page(data.name)
        return [page_ids[x] for x in sorted(page_ids.keys())]
                    
class Page(object):
    '''Preside over Pages Database Table Records'''

    def __init__(self, name):
        #self.data = Data().data.pages[name]
        self.data = data.getInstance().pages[name]

    @property
    def name(self):
        return self.data.name

    @property
    def pics(self):
        '''Using data's list of pic odicts
           Instatiate each and return list of Pic Objects
        '''
        return [Pic(p.name) for p in self.data.pics]

    def __repr__(self):
        return '<pages.Page(%s) object>' % self.name

from vlib import db
#from vlib.datatable import DataTable

from data import Data


from pagepics import PagePics

class Pics(object): # DataTable):
    '''Preside over Pics Database Table'''

    def __init__(self):
        self.data = Data().data.pics
        #self.db = db.getInstance()

        #DataTable.__init__(self, self.db, 'pics')
    
    def get(self, page=None):
        '''Given an optional page name, or None for All
           Return a list of Pic Objects
        '''
        if not page:
            return self.data

        o = []
        for pic in self.data:
            if pic.page == page:
                o.append(pic)
        return o

class Pic(object): #DataTable):
    '''Preside over Pics Data'''

    def __init__(self, name):
        self.data = Data().data.pics[name]

        '''
        #self.db = db.getInstance()
        #DataTable.__init__(self, self.db, 'pics')
        self.xdata = Data()
        #print self.xdata.data
        self.data = self.xdata.data['pics']
        #print 'x:', self.data
        self.__dict__.update(self.data)
        '''
    def get(self, name):
        return 'x'

    @property
    def pic_id(self):
        return 'x'
    @property
    def name(self):
        return self.data['name']

    @property
    def page_name(self):
        return self.data.page_name

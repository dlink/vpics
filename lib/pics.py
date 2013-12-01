from vlib import db
from vlib.datatable import DataTable

from pagepics import PagePics

class Pics(DataTable):
    '''Preside over Pics Database Table'''

    def __init__(self):
        self.db = db.getInstance()
        DataTable.__init__(self, self.db, 'pics')
        
    def get(self, filter=None):
        '''Given an optional SQL filter, or None for All
           Return a list of Pic Objects
        '''
        o = []
        for row in DataTable.get(self, filter):
            o.append(Pic(row['pic_id']))
        return o

class Pic(DataTable):
    '''Preside over Pics Database Table Records'''

    def __init__(self, pic_id):
        self.db = db.getInstance()
        DataTable.__init__(self, self.db, 'pics')
        self.data = self.get('pic_id = %s' % pic_id)[0]
        self.__dict__.update(self.data)

    @property
    def pages(self):
        if '_pages' not in self.__dict__:
            self._pages = []
            for row in PagePics().get('pic_id = "%s"' % self.pic_id):
                self._pages.append(row)
        return self._pages

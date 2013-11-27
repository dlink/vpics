from vlib import db
from vlib.datatable import DataTable

class Pages(DataTable):
    '''Preside over Pages Database Table'''

    def __init__(self):
        self.db = db.getInstance()
        DataTable.__init__(self, self.db, 'pages')
        
    def get(self, filter=None):
        '''Given an optional SQL filter, or None for All
           Return a list of Page Objects
        '''
        o = []
        for row in DataTable.get(self, filter):
            o.append(Page(row['page_id']))
        return o

class Page(DataTable):
    '''Preside over Pages Database Table Records'''

    def __init__(self, page_id):
        self.db = db.getInstance()
        DataTable.__init__(self, self.db, 'pages')
        self.data = self.get('page_id = %s' % page_id)[0]
        self.__dict__.update(self.data)
    

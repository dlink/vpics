from vlib import db
from vlib.datatable import DataTable

class PagePics(DataTable):
    '''Preside over the Page Pics many-to-many Database Table'''

    def __init__(self):
        self.db = db.getInstance()
        DataTable.__init__(self, self.db, 'page_pics')

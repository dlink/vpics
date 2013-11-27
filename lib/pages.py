from vlib import db
from vlib.datatable import DataTable

class Pages(DataTable):

    def __init__(self):
        self.db = db.getInstance()
        DataTable.__init__(self, self.db, 'pages')
        

print Pages().getTable()

from data import Data

class Pages(object):
    '''Preside over Pages Database Table'''

    def __init__(self):
        self.data = Data().data.pages
        
    def getAll(self):
        '''Return a list of Page Objects
        '''
        return self.data

class Page(object):
    '''Preside over Pages Database Table Records'''

    def __init__(self, name):
        self.data = Data().data.pages[name]

    @property
    def name(self):
        return self.data.name

    @property
    def pics(self):
        return self.data.pics


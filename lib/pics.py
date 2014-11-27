import data

class PicsError(Exception): pass

class Pics(object): # DataTable):
    '''Preside over Pics Data'''

    def __init__(self):
        self.data = data.getInstance()
    
    def get(self, page_name=None):
        '''Return list of instantiated Pic Objects
           for a given page_name, or for All if no page_name given
        '''
        if not page_name:
            return self.data.pics.values()

        if page_name not in self.data.pages:
            raise PicsError("Page '%s' not found" % page_name)

        return self.data[page_name]['pics']

class Pic(object):
    '''Preside over a single Pic's Data'''

    def __init__(self, name):
        self.__dict__.update(data.getInstance().pics[name])

import data

class Pics(object): # DataTable):
    '''Preside over Pics Data'''

    def __init__(self):
        self.data = data.getInstance().pics
    
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

class Pic(object):
    '''Preside over a single Pic's Data'''

    def __init__(self, name):
        self.__dict__.update(data.getInstance().pics[name])

import data
from pics import Pic

class Pages(object):
    '''Preside over Pages Data'''

    def __init__(self, dataset=None):
        self.data = dataset or data.getInstance()
        
    def getAll(self):
        '''Return a list of Page Objects'''
        return self.data.pages

    @property
    def site_name(self):
        return self.data.site_name

    @property
    def site_message(self):
        return self.data.site_message

    @property
    def first_page(self):
        '''Return and first page as an instantiated Page Class'''
        return Page(self.data.pages[0], self.data)

    @property
    def list(self):
        '''Return a list of instantiated Page objects in id order'''
        return [Page(x, self.data) for x in self.data.pages]


class PageError(Exception): pass

class Page(object):
    '''Preside over Pages Database Table Records'''

    def __init__(self, name, dataset=None):
        self.name = name

        self.data = dataset or data.getInstance()
        if name not in self.data.pages:
            raise PageError("Page '%s' not found." % name)
        self.__dict__.update(self.data[name])

    def __repr__(self):
        return '[pages.Page(%s) object]' % self.name

# Navigation - An HTML Partial

from vweb.html import * 
from pages import Pages

SP = '&nbsp;'

class Nav(object):
    def __init__(self):
        self.pages = Pages()

    def style_sheets(self):
        return 'css/nav.css'

    def nav(self, name=None):
        '''Draw Navigation Menu.
           Pass in the name of the current selection.
        '''

        menu = []
        for page in self.pages.list:
            menu.append([page.name, 'collection.py?id=%s' % page.name])

        # hard coding
        menu.append(['Shows'       , 'collection.py?id=shows'])
        menu.append(['About'       , 'about.py'])
        menu.append(['Contact Info', 'contact.py'])
            
        
        o = ''
        for item in menu:
            if item[0] == name:
                class_ = 'navLinkSelected'
            else:
                class_ = 'navLink'

            o += a(nobr(SP+SP+item[0]+SP+SP+SP), 
                   href=item[1], 
                   class_=class_)+br()
        o = ul(o)
        return div(o, id='nav')


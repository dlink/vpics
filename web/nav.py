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

        # menu item for each page
        menu = []
        for page in self.pages.list:
            menu.append([page.name, 'collection.py?id=%s' % page.name])

        # format menu items with links and classes
        o = ''
        for item in menu:
            if item[0] == name:
                class_ = 'navLinkSelected'
            else:
                class_ = 'navLink'

            menu_item_name = item[0].title()
            o += a(nobr(SP+SP+menu_item_name+SP+SP+SP),
                   href=item[1], 
                   class_=class_)+br()
        o = ul(o)
        return div(o, id='nav')


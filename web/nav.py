# Navigation - An HTML Partial

from vweb.html import * 

SP = '&nbsp;'

class Nav(object):

    def style_sheets(self):
        return 'css/nav.css'

    def nav(self, name=None):
        '''Draw Navigation Menu.
           Pass in the name of the current selection.
        '''
        menu = [
            ['Sculpture'   , 'collection.py?id=sculpture'],
            ['Drawings'    , 'collection.py?id=drawings'],
            ['Paintings'    , 'collection.py?id=paintings'],
            ['Shows'       , 'collection.py?id=shows'],
            ['About'       , 'about.py'],
            ['Contact Info', 'contact.py']
            ]
        
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


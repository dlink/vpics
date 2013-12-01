# Navigation - An HTML Partial

from vweb.html import * 

SP = '&nbsp;'

class Nav(object):

    def style_sheets(self):
        return 'css/nav.css'

    def nav(self):
        menu = [
            ['Sculpture'   , 'collection.py?id=sculpture'],
            ['Drawings'    , 'collection.py?id=drawings'],
            ['About'       , 'about.py'],
            ['Contact Info', 'contact.py']
            ]
        
        o = ''
        for item in menu:
            if item[0] == 'Sculpture':
                class_ = 'navLinkSelected'
            else:
                class_ = 'navLink'

            o += a(nobr(SP+SP+item[0]+SP+SP+SP), 
                   href=item[1], 
                   class_=class_)+br()
        o = ul(o)
        return div(o, id='nav')


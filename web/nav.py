# Navigation - An HTML Partial

from vweb.html import * 

class Nav(object):

    def style_sheets(self):
        return 'css/nav.css'

    def nav(self):
        o = ul(' '.join([li(a('About', href='about.py')),
                         li(a('Sculpture', href='collection.py?id=sculpture')),
                         li('Drawings'),
                         li(nobr('Contact Info'))]))
        return div(o, id='nav')


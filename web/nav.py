# Navigation - An HTML Partial

from vweb.html import * 

class Nav(object):

    def style_sheets(self):
        return 'css/nav.css'

    def nav(self):
        o = ul(' '.join([li('About'),
                         li('Sculpture'),
                         li('Drawings'),
                         li('Contact Info')]))
        return div(o, id='nav')


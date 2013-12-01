#!/usr/bin/env python

from vlib import conf

from vweb.htmlpage import HtmlPage
from vweb.htmltable import HtmlTable
from vweb.html import *

from nav import Nav

class Contact(HtmlPage):

    def __init__(self):
        HtmlPage.__init__(self, 'Pics Page')
        self.style_sheets.append('css/vpics.css')
        #self.style_sheets.append('css/contact.css')

        # navigation
        self.nav = Nav()
        self.style_sheets.append(self.nav.style_sheets())

    def getHtmlContent(self):
        return \
            self.header() +\
            self.navAndDisplayArea()
                       
    def navAndDisplayArea(self):
        table = HtmlTable()
        table.addRow([self.nav.nav(name='Contact Info'),
                      self.displayArea()])
        table.setRowVAlign(1,'top')
        return center(table.getTable())

    def header(self):
        text = 'David Link'
        return div(h2(text), id='header')

    def displayArea(self):
        return div(text(), id='displayArea')

def text():
    return '''
<div style="padding: 20px;">
David Link<br>
Putnam Valley, NY<br>
<br>
914-629-5723<br>
<br>
dvlink@gmail.com<br>
<br>
d a v i d l i n k a r t . c o m
</div>
'''

Contact().go()


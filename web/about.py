#!/usr/bin/env python

from vlib import conf

from vweb.htmlpage import HtmlPage
from vweb.htmltable import HtmlTable
from vweb.html import *

from nav import Nav

class About(HtmlPage):

    def __init__(self):
        HtmlPage.__init__(self, 'Pics Page')
        #self.conf = conf.getInstance()        
        self.style_sheets.append('css/vpics.css')

        # navigation
        self.nav = Nav()
        self.style_sheets.append(self.nav.style_sheets())

        #self.pages = Pages()
        #self.page = None

    def getHtmlContent(self):
        return \
            self.header() +\
            self.navAndDisplayArea()
                       
    def navAndDisplayArea(self):
        table = HtmlTable()
        table.addRow([self.nav.nav(),
                      self.displayArea()])
        table.setRowVAlign(1,'top')
        return center(table.getTable())

    def header(self):
        text = 'David Link'
        return div(h2(text), id='header')

    def displayArea(self):
        return text()

def text():
    return '''
<h3>Elegance and Design</h3>

<p>I love form and shape.  I Draw, I Paint and I Sculpt.  Everything starts from Drawing.  I draw realistically and, I draft designs.  Sculpture start as a drawing.  I make hundreds of sketches of sculptures, that fill notebooks.  I exploring subtle differences in angles and proportions.  I strive to find the right piece, elegant in design, and shows simple harmony in form, before I choosing one to build.</p>

<p>My Sculpture is Mathematical.  It is interesting to look at from all angles.   It is an interplays of forms and space.  Line can be a three dimensional sold.  Sculpture is made up of basic geometric shapes.  When form is reduced to simple shapes, then the basic elements or Art:  Balance, Rhythm, Harmony, and Beauty, are revealed.</p>

<p>I studied Painting, Drawing and Sculpture at SUNY Purchase.   I became greatly inspired by such artists such as 

<a href=https://www.google.com/search?q=frank+stella&espv=210&es_sm=91&source=lnms&tbm=isch&sa=X&ei=QZmaUpmGE5TEsATBsoGgCA&ved=0CAkQ_AUoAQ&biw=1162&bih=613" target="_blank">Frank Stella</a>, 

Ellsworth Kelly, Donald Judd, Tony Smith, and Sol LeWitt, and the Minimalist Movement in Sculpture.</p>
'''

About().go()


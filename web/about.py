#!/usr/bin/env python

from vlib import conf

from vweb.htmlpage import HtmlPage
from vweb.htmltable import HtmlTable
from vweb.html import *

from nav import Nav

class About(HtmlPage):

    def __init__(self):
        HtmlPage.__init__(self, 'Pics Page')
        self.style_sheets.append('css/vpics.css')
        self.style_sheets.append('css/about.css')

        # navigation
        self.nav = Nav()
        self.style_sheets.append(self.nav.style_sheets())

    def getHtmlContent(self):
        return \
            self.header() +\
            self.navAndDisplayArea()
                       
    def navAndDisplayArea(self):
        table = HtmlTable()
        table.addRow([self.nav.nav(name='About'),
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
<table>
  <tr>
    <td valign="top">
      <center><img src="images/Cube_Drawing.png"/></center>
      <p>&nbsp;</p>
      <img src="images/Self.jpg"/>
      <img src="images/David_Link.png"/>
    </td>
    <td>
<h3>Elegance and Design</h3>


<p>I love form and shape.  I draw, paint and sculpt.  Everything starts from drawing.  I draw realistically and, I draft designs.  Sculpture start as a drawing.  I make hundreds of sketches of sculptures, that fill notebooks.  I exploring subtle differences in angles and proportions.  I strive to find the right piece, elegant in design, and shows simple harmony in form, before I choosing one to build.</p>

<p>My Sculpture is Mathematical.  It is interesting to look at from all angles.   It is an interplays of forms and space.  Line can be a three dimensional sold.  Sculpture is made up of basic geometric shapes.  When form is reduced to simple shapes, then the basic elements or Art:  Balance, Rhythm, Harmony, and Beauty, are revealed.</p>

<p>I studied Painting, Drawing and Sculpture at SUNY Purchase.   I became greatly inspired by such artists such as 
<a href="http://images.google.com/images?q=frank+stella" target="_blank">Frank Stella</a>, 
<a href="http://images.google.com/images?q=ellsworth+kelly" target="_blank">Ellsworth Kelly</a>,
<a href="http://images.google.com/images?q=Donald+Judd" target="_blank">Donald Judd</a>, 
<a href="http://images.google.com/images?q=Tony+Smith" target="_blank">Tony Smith</a>, and 
<a href="http://images.google.com/images?q=Sol+LeWitt" target="_blank">Sol LeWitt</a>, and 
the <a href="http://en.wikipedia.org/wiki/Minimalism">Minimalist Movement</a> in Sculpture.</p>


<p>&nbsp;</p>

<h3>Shows and Experience</h3>

<p>Recent</p>
<ul>
  <li>Dec 2013 - Jan 2014: <a href="http://baugallery.com">Bau Gallery<a/>, Beacon, NY - Group Show: <i>Saints and Sinners</i>
  <li>Dec 2013 - Jan 2014: <a href="http://www.catalystgallery.com/">The Catalyst Gallery</a>, Beacon, NY - Group Show
</ul>

<pe>Previous</p>
<ul>
  <li> Manhole Drawing Series.  Ossining Art Council, 1995
  <li> Public Mural: Computer Motif, Cuernavaca, Mexico, House Paint, 12'x8', 1992
  <li> Public Mural: Repro of D'Vinci's Annunciation, Cuautla, Mexico, House Paint, 8'x3', 1990
  <li> Public Mural: Biomophic Forms, Oyster Bay, NY, House Paint, 25'x8', 1983 
  <li> Large Outdoor Sculpture, Purchase, NY, 8'x4'x4', steel, 1982
  <li> Large Outdoor Sculpture, Oyster Bay, NY, 10'x10'x10', plywood and 2x4s, 1977
</ul>


<p>&nbsp;</p>

<h3>Education</h3>
<ul>
  <li>SUNY Purchase, NY - Fine Art, 1981- 1984
  <li>SUNY Oneonta, NY - Mathematics, 1979 - 1981
</ul>

   </td>
</tr>
</table>
'''

About().go()


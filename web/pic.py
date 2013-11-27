#!/usr/bin/env python

from vlib import conf

from vweb.htmlpage import HtmlPage
from vweb.htmltable import HtmlTable
from vweb.html import *

class Pics(HtmlPage):

    def __init__(self):
        HtmlPage.__init__(self, 'Pics')
        self.conf = conf.getInstance()        
        self.style_sheets.append('css/pics.css')

    def getHtmlContent(self):
        return \
            self.header() +\
            self.navAndDisplayArea()
           
    def navAndDisplayArea(self):
        table = HtmlTable()
        table.addRow([self.nav(),
                      self.displayArea()])
        table.setRowVAlign(1,'top')
        return center(table.getTable())

    def header(self):
        text = 'David Link'
        return div(h2(text), id='header')

    def nav(self):
        o = ul(' '.join([li('About'),
                         li('Sculpture'),
                         li('Drawings'),
                         li('Contact Info')]))
        return div(o, id='nav')

    def displayArea(self):
        return self.pic()

    def pic(self):
        pic_url = "/%s/%s" % (self.conf.media_dir, 'Sinner.jpg')
        pic_img = img(src=pic_url, class_='picImage')
        caption = self.picCaption() 
        return div(pic_img + caption, class_='pic')

            
    def picCaption(self):
        #return p('<i>Sinner. </i><small>2013. Wood. 12 x 6 x 6 inches</small>',
        #         class_='picCaption')
        return div('<i>Bent Rectangle with House Motif. </i><small>2013. Wood. 12 x 6 x 6 inches</small>',
                 class_='picCaption')

Pics().go()


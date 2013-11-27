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
            self.nav() + \
            self.displayArea()

    def header(self):
        return div('header', id='header')
                   

    def nav(self):
        return div('nav', id='nav')

    def displayArea(self):
        table = HtmlTable(id='displayTable')
        for r in range(0,3):
            row = []
            for c in range(0,3):
                row.append(center(self.pic()))
            table.addRow(row)
        return table.getTable()

    def pic(self):
        pic_url = "/%s/%s" % (self.conf.media_dir, 'Sinner_300px.jpg')
        pic_img = img(src=pic_url, class_='picImage')
        caption = self.picCaption() #p('Picture Caption', class_='picCaption')
        return span(pic_img + caption, class_='pic')
            
    def picCaption(self):
        return p('<b>Sinner</b> (2013)<br>Wood.  Height: 12in.', class_='picCaption')
Pics().go()


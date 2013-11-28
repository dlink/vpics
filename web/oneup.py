#!/usr/bin/env python

from vlib import conf

from vweb.htmlpage import HtmlPage
from vweb.htmltable import HtmlTable
from vweb.html import *

from pics import Pics, Pic

from nav import Nav

DEFAULT_PIC_ID = 1

class Oneup(HtmlPage):

    def __init__(self):
        HtmlPage.__init__(self, 'Oneup')
        self.conf = conf.getInstance()        
        self.style_sheets.append('css/oneup.css')

        # nav
        self.nav = Nav()
        self.style_sheets.append(self.nav.style_sheets())

        self.pics = Pics()
        self.pic = None

    def process(self):
        # get pic_id from form
        if 'id' in self.form:
            pic_id = self.form['id'].value
        else:
            pic_id = DEFAULT_PIC_ID

        # get Page Object
        if pic_id.isdigit():
            self.pic = Pic(pic_id)
        else:
            self.pic = self.pics.get('name = "%s"' % pic_id)[0]

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
        return self.pic_div()

    def pic_div(self):
        pic_url = "/%s/%s" % (self.conf.media_dir, self.pic.filename)
        pic_img = img(src=pic_url, class_='picImage')
        caption = self.picCaption() 
        return div(pic_img + caption, class_='pic')

    def picCaption(self):
        return div('<i>%s </i><small>%s</small>' % (self.pic.name,
                                                    self.pic.caption),
                 class_='picCaption')

Oneup().go()


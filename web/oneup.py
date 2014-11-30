#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.htmltable import HtmlTable
from vweb.html import *

from env import Env
from pages import Page
from pics import Pics, Pic
from nav import Nav

class Oneup(HtmlPage):

    def __init__(self):
        HtmlPage.__init__(self, 'Oneup')
        self.style_sheets.append('css/vpics.css')
        self.style_sheets.append('css/oneup.css')
        self.javascript_src.append('js/googleanalytics.js')

        # nav
        self.nav = Nav()
        self.style_sheets.append(self.nav.style_sheets())

        self.env = Env()
        self.pics = Pics()
        self.pic = None

    def process(self):
        pic_name = self.form['id'].value
        self.pic = Pic(pic_name)

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
        return div(self.pic_div(), id='displayArea')

    def pic_div(self):
        pic_url = "/%s/%s/%s" % (self.env.media_url,
                                 self.pic.page_name,
                                 self.pic.filename)
        pic_img = img(src=pic_url, class_='picImage')
        picNav = self.picNav()
        caption = self.picCaption() 
        description = self.picDescription()
        return div(picNav + pic_img + caption + hr() + description,
                   class_='pic')

    def picNav(self):
        page = Page(self.pic.page_name)

        prev_pic_name = None
        next_pic_name = None
        old_pic_name = None
        found = 0

        # loop thru first page of pics, find prev and next pic_names
        for pic in page.pics:
            pic_name = pic.name
            if found:
                next_pic_name = pic_name
                break
            if pic_name == self.pic.name:
                if old_pic_name:
                    prev_pic_name = old_pic_name
                found = 1
            old_pic_name = pic_name

        #prev
        if prev_pic_name:
            prev = a('prev', href='oneup.py?id=%s' % prev_pic_name)
        else:
            prev = font('prev', color='lightgrey')

        # next
        if next_pic_name:
            next = a('next', href='oneup.py?id=%s' % next_pic_name)
        else:
            next = font('next', color='lightgrey')
        return div('%s | %s' % (prev, next), class_='picNav')

    def picCaption(self):
        return div('<i>%s </i><small>%s</small>' % (self.pic.name,
                                                    self.pic.caption),
                 class_='picCaption')

    def picDescription(self):
        return div(self.pic.description or '', class_='picDescription')

if __name__ == '__main__':
    Oneup().go()


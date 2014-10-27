#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.htmltable import HtmlTable
from vweb.html import *

from env import Env
from pages import Pages, Page
from nav import Nav

NUM_COLS = 3
THUMBNAILS = '200px'

class Collection(HtmlPage):

    def __init__(self):
        HtmlPage.__init__(self, 'Pics Page')
        self.style_sheets.append('css/vpics.css')
        self.style_sheets.append('css/collection.css')
        self.javascript_src.append('js/googleanalytics.js')

        # navigation
        self.nav = Nav()
        self.style_sheets.append(self.nav.style_sheets())

        self.env = Env()
        self.pages = Pages()
        self.page = None

    def getHtmlContent(self):
        return \
            self.header() +\
            self.messageLine() +\
            self.navAndDisplayArea()
           
    def process(self):
        if 'id' in self.form:
            self.page = Page(self.form['id'].value)
        else:
            self.page = self.pages.first_page

    def messageLine(self):
        msg_lines = ['user message']
        return center('<br/>'.join(msg_lines))
    
    def navAndDisplayArea(self):
        table = HtmlTable()
        table.addRow([self.nav.nav(self.page.name),
                      self.displayArea()])
        table.setRowVAlign(1,'top')
        return center(table.getTable())

    def header(self):
        text = 'David Link'
        return div(h2(text), id='header')

    def displayArea(self):
        if not self.page:
            return self.pageNotFound()

        num_pics = len(self.page.pics)
        num_rows = ((num_pics-1)/NUM_COLS)+1

        table = HtmlTable(id='displayTable')
        i = 0
        for r in range(0, num_rows):
            row = []
            for c in range(0, NUM_COLS):
                if i < num_pics:
                    row.append(self.pic_div(i))
                    i += 1
            table.addRow(row)
            table.setRowVAlign(table.rownum, 'top')
        return div(table.getTable(), id='displayArea')

    def pic_div(self, i):
        '''
        <center>
           <div class="pic">
              <a href="/oneup.py?id=NAME">
                 <img src="URL" class="picImage">
                 <div class="picCaption">
                    <i>NAME </i>
                    <small>CAPTION</small>
                 <div>
              </a>
           <div>
        </center>
        '''
        # hard coding
        #media_dir="/data/vpics"
        media_dir="dev-vpics/images"

        pic_url = "/%s/%s/%s" % (media_dir, THUMBNAILS,
                                 self.page.pics[i].filename)
        pic_img = img(src=pic_url, class_='picImage')
        caption = self.picCaption(i) 
        href = "%s/oneup.py?id=%s" % (self.env.base_url, 
                                      self.page.pics[i].name)
        return center(div(a(pic_img + caption, href=href), class_='pic'))

    def picCaption(self, i):
        return div('<i>%s </i><small>%s</small>' % (self.page.pics[i].name,
                                                    self.page.pics[i].caption),
                 class_='picCaption')

    def pageNotFound(self):
        return div(p('No page found.'))

if __name__ == '__main__':
    Collection().go()


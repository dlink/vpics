#!/usr/bin/env python

from vlib import conf

from vweb.htmlpage import HtmlPage
from vweb.htmltable import HtmlTable
from vweb.html import *

from pages import Pages, Page

DEFAULT_PAGE_ID = '1'
NUM_COLS = 3

class PicsPage(HtmlPage):

    def __init__(self):
        HtmlPage.__init__(self, 'Pics Page')
        self.conf = conf.getInstance()        
        self.style_sheets.append('css/pics.css')

        self.pages = Pages()
        self.page = None

    def getHtmlContent(self):
        return \
            self.header() +\
            self.navAndDisplayArea()
           
    def process(self):
        # get page_id from form
        if 'id' in self.form:
            page_id = self.form['id'].value
        else:
            page_id = DEFAULT_PAGE_ID

        # get Page Object
        if page_id.isdigit():
            self.page = Page(page_id)
        else:
            self.page = self.pages.get('name = "%s"' % page_id)

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
        pic_url = "/%s/%s" % (self.conf.media_dir, self.page.pics[i].filename)
        pic_img = img(src=pic_url, class_='picImage')
        caption = self.picCaption(i) 
        href = "/pic.py"
        return div(pic_img + caption, class_='pic')

            
    def picCaption(self, i):
        return div('<i>%s </i><small>%s</small>' % (self.page.pics[i].name,
                                                    self.page.pics[i].caption),
                 class_='picCaption')

PicsPage().go()


#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.htmltable import HtmlTable
from vweb.html import *

from pages import Pages, Page

from nav import Nav

DEFAULT_PAGE_ID = '1'
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

        self.pages = Pages()
        self.page = None

    def getHtmlContent(self):
        return \
            self.header() +\
            self.messageLine() +\
            self.navAndDisplayArea()
           
    def process(self):
        self.page = self.pages.first_page
        """
        # get page_id from form
        if 'id' in self.form:
            page_id = self.form['id'].value
        else:
            page_id = DEFAULT_PAGE_ID

        # get Page Object
        if page_id.isdigit():
            self.page = Page(page_id)
        else:
            results = self.pages.get('name = "%s"' % page_id)
            if results:
                self.page = results[0]
               """
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
        self.debug_msg += p('num_pics: %s' % num_pics)
        self.debug_msg += p('num_rows: %s' % num_rows)

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
        #media_dir="/data/vpics"
        media_dir="dev-vpics/images"

        pic_url = "/%s/%s/%s" % (media_dir, THUMBNAILS,
                                 self.page.pics[i].filename)
        #pic_url = "undetermined"
        pic_img = img(src=pic_url, class_='picImage')
        caption = self.picCaption(i) 
        href = "/oneup.py?id=%s" % self.page.pics[i].name
        return center(div(a(pic_img + caption, href=href), class_='pic'))

    def picCaption(self, i):
        return div('<i>%s </i><small>%s</small>' % (self.page.pics[i].name,
                                                    self.page.pics[i].caption),
                 class_='picCaption')

    def pageNotFound(self):
        return div(p('No page found.'))

if __name__ == '__main__':
    Collection().go()


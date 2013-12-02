#!/usr/bin/env python

from vlib import conf

from vweb.htmlpage import HtmlPage
from vweb.htmltable import HtmlTable
from vweb.html import *

from pages import Page
from pics import Pics, Pic

from nav import Nav

DEFAULT_PIC_ID = 1

class Oneup(HtmlPage):

    def __init__(self):
        HtmlPage.__init__(self, 'Oneup')
        self.conf = conf.getInstance()        
        self.style_sheets.append('css/vpics.css')
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

        # get Pic Object
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
        return div(self.pic_div(), id='displayArea')

    def pic_div(self):
        collections = ''  #self.picCollections()
        pic_url = "/%s/%s" % (self.conf.media_dir, self.pic.filename)
        pic_img = img(src=pic_url, class_='picImage')
        picNav = self.picNav()
        caption = self.picCaption() 
        description = self.picDescription()
        return div(collections + pic_img + picNav + caption + hr() + description, 
                   class_='pic')

    def picCollections(self):
        collections = []
        for row in self.pic.pages:
            page = Page(row['page_id'])
            
            collections.append(a(page.name, href='collection.py?id=%s' 
                                 % page.name))
        return div('Tags: ' + ', '.join(collections), class_='picCollections')

    def picNav(self):
        page = Page(self.pic.pages[0]['page_id'])

        prev_pic_id = None
        next_pic_id = None
        old_pic_id = None
        found = 0

        # loop thru first page of pics, find prev and next pic_ids
        for pic in page.pics:
            pic_id = pic.pic_id
            if found:
                next_pic_id = pic_id
                break
            if pic_id == self.pic.pic_id:
                if old_pic_id:
                    prev_pic_id = old_pic_id
                found = 1
            old_pic_id = pic_id

        #prev
        if prev_pic_id:
            prev = a('prev', href='oneup.py?id=%s' % prev_pic_id)
        else:
            prev = font('prev', color='lightgrey')

        # next
        if next_pic_id:
            next = a('next', href='oneup.py?id=%s' % next_pic_id)
        else:
            next = font('next', color='lightgrey')
        return '%s | %s' % (prev, next)

    def picCaption(self):
        return div('<i>%s </i><small>%s</small>' % (self.pic.name,
                                                    self.pic.caption),
                 class_='picCaption')

    def picDescription(self):
        return div(self.pic.description or '', class_='picDescription')

Oneup().go()


#!/usr/bin/env python

from vweb.htmlpage import HtmlPage

class Pics(HtmlPage):
    
    def getHtmlContent(self):
        return 'hi there'

Pics().go()


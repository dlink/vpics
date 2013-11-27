#!/usr/bin/env python

import unittest

from pages import Pages, Page

PAGE_ID = 1
PAGE_NAME = 'Sculpture'

class TestPages(unittest.TestCase):

    def setUp(self):
        self.pages = Pages()

    def test_pages_list_all(self):
        num = len(self.pages.get())
        self.assertTrue(num)

    def test_page_get(self):
        page = Page(PAGE_ID)
        self.assertTrue(PAGE_ID, page.page_id)

    def test_page_get_name(self):
        page = self.pages.get(filter="name = '%s'" % PAGE_NAME)[0]
        self.assertTrue(PAGE_NAME, page.name)
                           
    def test_page_pics(self):
        page = Page(PAGE_ID)
        self.assertTrue(len(page.pics))

if __name__ == '__main__':
    unittest.main()

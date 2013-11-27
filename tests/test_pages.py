#!/usr/bin/env python

import unittest

from pages import Pages, Page

PAGE_ID = 1

class TestPages(unittest.TestCase):

    def setUp(self):
        self.pages = Pages()
        self.page  = Page(PAGE_ID)

    def test_pages_list_all(self):
        num = len(self.pages.get())
        self.assertTrue(num)

    def test_page_get(self):
        self.assertTrue(PAGE_ID, self.page.page_id)

if __name__ == '__main__':
    unittest.main()

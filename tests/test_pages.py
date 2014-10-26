#!/usr/bin/env python

import unittest

from pages import Pages, Page

PAGE_NAME = 'Sculptures'

class TestPages(unittest.TestCase):

    def setUp(self):
        self.pages = Pages()

    def test_pages_list_all(self):
        num = len(self.pages.getAll())
        self.assertTrue(num>0)

    def test_page_get(self):
        page = Page(PAGE_NAME)
        self.assertEqual(PAGE_NAME, page.name)

    def test_page_pics(self):
        page = Page(PAGE_NAME)
        self.assertTrue(len(page.pics)>0)

    def test_first_page(self):
        page = self.pages.first_page
        self.assertEqual(page.name, PAGE_NAME)

if __name__ == '__main__':
    unittest.main()

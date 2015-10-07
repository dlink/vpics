#!/usr/bin/env python

import unittest

from pics import Pics, Pic

#PIC_FILENAME = 'Sinner.jpg'
PIC_NAME = 'Sinner'
PAGE_NAME = 'sculptures'

class TestPics(unittest.TestCase):

    def setUp(self):
        self.pics = Pics()

    def test_pics_get(self):
        names = [x['name'] for x in self.pics.get(PAGE_NAME)]
        self.assertTrue(PIC_NAME in names)

    def test_pics_list_all(self):
        num = len(self.pics.get())
        self.assertTrue(num)

    def test_pic_get_filename(self):
        pic = Pic(PIC_NAME)
        self.assertEqual(PIC_NAME, pic.name)
        
    def test_pic_page(self):
        pic = Pic(PIC_NAME)
        self.assertEqual(pic.page_name, PAGE_NAME)

if __name__ == '__main__':
    unittest.main()

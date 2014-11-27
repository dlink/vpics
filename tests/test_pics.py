#!/usr/bin/env python

import unittest

from pics import Pics, Pic

PIC_FILENAME = 'Sinner.jpg'
PAGE_NAME = 'sculptures'

class TestPics(unittest.TestCase):

    def setUp(self):
        self.pics = Pics()

    def test_pics_get(self):
        filenames = [x['filename'] for x in self.pics.get(PAGE_NAME)]
        self.assertTrue(PIC_FILENAME in filenames)

    def test_pics_list_all(self):
        num = len(self.pics.get())
        self.assertTrue(num)

    def test_pic_get_filename(self):
        pic = Pic(PIC_FILENAME)
        self.assertEqual(PIC_FILENAME, pic.filename)
        
    #def test_pic_page(self):
    #    pic = Pic(PIC_FILENAME)
    #    self.assertEqual(pic.page_name, PAGE_FILENAME)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python

import unittest

from pics import Pics, Pic

PIC_ID = 1
PIC_NAME = 'Sinner'
PAGE_NAME = 'Sculptures'

class TestPics(unittest.TestCase):

    def setUp(self):
        self.pics = Pics()

    def test_pics_list_all(self):
        num = len(self.pics.get())
        self.assertTrue(num)

    #def test_pic_get_id(self):
    #    pic = Pic(PIC_ID)
    #    self.assertEqual(PIC_ID, pic.pic_id)

    def test_pic_get_name(self):
        #pic = self.pics.get(PIC_NAME)[0] #filter="name = '%s'" % PIC_NAME)[0]
        pic = Pic(PIC_NAME)
        self.assertTrue(PIC_NAME, pic.name)
                           
    def test_pic_page(self):
        pic = Pic(PIC_NAME)
        self.assertEqual(pic.page_name, PAGE_NAME)

if __name__ == '__main__':
    unittest.main()

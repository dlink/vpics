#!/usr/bin/env python

import unittest

from pics import Pics, Pic

PIC_ID = 1
PIC_NAME = 'Sinner'

class TestPics(unittest.TestCase):

    def setUp(self):
        self.pics = Pics()

    def test_pics_list_all(self):
        num = len(self.pics.get())
        self.assertTrue(num)

    def test_pic_get(self):
        pic = Pic(PIC_ID)
        self.assertTrue(PIC_ID, pic.pic_id)

    def test_pic_get_name(self):
        pic = self.pics.get(filter="name = '%s'" % PIC_NAME)[0]
        self.assertTrue(PIC_NAME, pic.name)
                           
    def test_pic_pages(self):
        pic = Pic(PIC_ID)
        self.assertTrue(len(pic.pages))

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python

import unittest

import data

class TestData(unittest.TestCase):

    def test_single_instance(self):
        a = data.getInstance()
        b = data.getInstance()
        a.testvalue = 1
        self.assertTrue('testvalue' in b);

if __name__ == '__main__':
    unittest.main()

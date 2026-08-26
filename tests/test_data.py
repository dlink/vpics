#!/usr/bin/env python3

import os
from pathlib import Path
import unittest

import data

TEST_CONFIG = Path(__file__).with_name('testconf.yml')

class TestData(unittest.TestCase):

    def setUp(self):
        data.configure(TEST_CONFIG)

    def test_single_instance(self):
        a = data.getInstance()
        b = data.getInstance()
        a.testvalue = 1
        self.assertTrue('testvalue' in b)

    def test_explicit_config_does_not_require_environment(self):
        os.environ.pop('VCONF', None)
        dataset = data.configure(TEST_CONFIG)
        self.assertEqual('Test Artworks', dataset.site_name)

    def test_picture_defaults_and_html_page(self):
        dataset = data.getInstance()
        sinner = dataset.pics['Sinner']
        self.assertEqual('', sinner.description)
        self.assertEqual('sculptures', sinner.page_name)
        self.assertEqual('about.html', dataset.about.html.filename)

if __name__ == '__main__':
    unittest.main()

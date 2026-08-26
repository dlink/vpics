#!/usr/bin/env python3

import os
from pathlib import Path
import unittest

import data
from pages import Pages
from pics import Pic, Pics


SEBASTIAN_CONFIG = os.environ.get('VPICS_SEBASTIAN_CONFIG')


@unittest.skipUnless(SEBASTIAN_CONFIG, 'VPICS_SEBASTIAN_CONFIG not set')
class TestSebastianPortfolio(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = Path(SEBASTIAN_CONFIG)
        cls.dataset = data.configure(cls.config)

    def test_site_identity_and_ordered_sections(self):
        pages = Pages(self.dataset)
        self.assertEqual('Sebastian Link', pages.site_name)
        self.assertEqual('drawing', pages.first_page.name)
        self.assertEqual(11, len(pages.getAll()))
        self.assertEqual(
            ['drawing', 'painting', 'photoshop', 'illustrator',
             'illustrator2', 'animation', 'videos', 'games', '3D',
             'music', 'about'],
            pages.getAll())

    def test_picture_catalog(self):
        pictures = Pics(self.dataset)
        self.assertEqual(92, len(pictures.get()))
        guts = Pic('Guts', self.dataset)
        self.assertEqual('Guts.png', guts.filename)
        self.assertEqual('drawing', guts.page_name)
        self.assertEqual('Drawing, 2023', guts.caption)

    def test_html_sections(self):
        expected = {
            'animation': 'animation.phtml',
            'videos': 'videos.phtml',
            'games': 'games.phtml',
            'music': 'music.phtml',
            'about': 'about.phtml',
        }
        actual = {
            name: self.dataset[name].html.filename
            for name in expected
        }
        self.assertEqual(expected, actual)

    def test_referenced_media_exists(self):
        media_root = self.config.parent
        missing_originals = []
        missing_thumbnails = []
        for page_name in self.dataset.pages:
            page = self.dataset[page_name]
            for picture in page.pics:
                if not (media_root / page_name / picture.filename).is_file():
                    missing_originals.append(
                        '%s/%s' % (page_name, picture.filename))
                if not (media_root / page_name / '300px' /
                        picture.filename).is_file():
                    missing_thumbnails.append(
                        '%s/300px/%s' % (page_name, picture.filename))

        self.assertEqual(
            ['illustrator2/Amazon Postcard Back2.png'],
            missing_originals)
        self.assertEqual([], missing_thumbnails)


if __name__ == '__main__':
    unittest.main()

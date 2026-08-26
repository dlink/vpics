#!/usr/bin/env python3

import os
from pathlib import Path
import sys
import unittest


WEB_DIR = Path(__file__).parents[1] / 'web'
if str(WEB_DIR) not in sys.path:
    sys.path.insert(0, str(WEB_DIR))

TEST_CONFIG = Path(__file__).with_name('testconf.yml')
SEBASTIAN_CONFIG = os.environ.get('VPICS_SEBASTIAN_CONFIG')
os.environ['VCONF'] = str(TEST_CONFIG)

from app import app, configure


class TestWebApplication(unittest.TestCase):

    def setUp(self):
        configure(TEST_CONFIG)
        self.client = app.test_client()

    def test_home_and_page_routes(self):
        root = self.client.get('/', follow_redirects=True)
        page = self.client.get('/page/paintings')
        self.assertEqual(200, root.status_code)
        self.assertIn(b'Test Artworks', root.data)
        self.assertIn(b'Sinner', root.data)
        self.assertEqual(200, page.status_code)
        self.assertIn(b'Blue Study', page.data)

    def test_legacy_collection_route(self):
        response = self.client.get('/collection.py?id=paintings')
        self.assertEqual(301, response.status_code)
        self.assertEqual('/page/paintings', response.location)

    def test_legacy_and_clean_oneup_routes(self):
        legacy = self.client.get('/oneup.py?id=Sinner')
        clean = self.client.get('/pic/Sinner')
        self.assertEqual(301, legacy.status_code)
        self.assertEqual('/pic/Sinner', legacy.location)
        self.assertEqual(200, clean.status_code)
        self.assertIn(b'/test-media/sculptures/Sinner.jpg', clean.data)

    def test_unknown_page_and_picture_are_not_found(self):
        self.assertEqual(404, self.client.get('/page/missing').status_code)
        self.assertEqual(404, self.client.get('/pic/missing').status_code)

    def test_script_name_prefixes_application_urls(self):
        response = self.client.get(
            '/page/sculptures',
            environ_overrides={'SCRIPT_NAME': '/portfolio'})
        self.assertEqual(200, response.status_code)
        self.assertIn(b'href="/portfolio/css/vpics.css"', response.data)
        self.assertIn(b'href="/portfolio/pic/Sinner"', response.data)


@unittest.skipUnless(SEBASTIAN_CONFIG, 'VPICS_SEBASTIAN_CONFIG not set')
class TestSebastianWebApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        configure(
            SEBASTIAN_CONFIG,
            thumbnail_dir='300px',
            page_columns={'illustrator2': 1})
        cls.client = app.test_client()

    def test_drawing_page_uses_300px_thumbnails(self):
        response = self.client.get('/page/drawing')
        self.assertEqual(200, response.status_code)
        self.assertIn(
            b'/sebastianlinkmusic/media/drawing/300px/Guts.png',
            response.data)

    def test_illustrator_two_uses_one_column(self):
        response = self.client.get('/page/illustrator2')
        self.assertEqual(200, response.status_code)
        self.assertIn(b'--vpics-columns: 1', response.data)

    def test_html_section_is_rendered(self):
        response = self.client.get('/page/about')
        self.assertEqual(200, response.status_code)
        self.assertIn(b'Sebastian_Link_Resume.pdf', response.data)

    def test_oneup_navigation_and_encoded_media(self):
        response = self.client.get('/pic/Self%20Portrait')
        self.assertEqual(200, response.status_code)
        self.assertIn(b'Self%20Portrait.jpg', response.data)
        self.assertIn(b'previous', response.data)
        self.assertIn(b'next', response.data)


if __name__ == '__main__':
    unittest.main()

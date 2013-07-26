#!/usr/bin/env python

import unittest
from wordpress.wordpress import WordPress

class WordPressTest(unittest.TestCase):
    
    def setUp(self):
        self.blog = WordPress('boycook.wordpress.com')
    
    def test_get_posts(self):
        self.blog.get_posts()

    def test_get_post(self):
        self.blog.get_post('100')

if __name__ == '__main__':
    unittest.main()
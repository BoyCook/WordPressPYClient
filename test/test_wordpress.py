#!/usr/bin/env python

import unittest
from wordpress.wordpress import WordPress


class WordPressTest(unittest.TestCase):
    def setUp(self):
        self.blog = WordPress('boycook.wordpress.com')

    def test_get_posts(self):
        posts = self.blog.get_posts()
        for post in posts:
            print str(post['ID']) + ' - ' + str(post['title']) 

    def test_get_post(self):
        # TODO - assertions
        post = self.blog.get_post('100')
        id = post['ID']
        print 'ID' + str(id)
        # post['content']
        # post['modified']
        # post['created_at']
        # post['modified']
        # post['excerpt']
        # post['title']
        # post['URL']


if __name__ == '__main__':
    unittest.main()
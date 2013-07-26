"""
A WordPress client written in Python
"""
# Using the WordPress REST API https://public-api.wordpress.com/rest/v1
# See http://developer.wordpress.com/docs/api

__author__ = "Craig Cook (BoyCook)"
__version__ = "0.0.1"

import json
import httplib2


class WordPressException(Exception):
    """
    Generic WordPress Exception
    """


class WordPress():
    BASE_URL = 'https://public-api.wordpress.com/rest/v1'

    def __init__(self, site):
        self.site = site
        self._http = httplib2.Http()

    def get_posts(self):
        url = self.BASE_URL + '/sites/' + self.site + '/posts'
        posts = self._http_get(url)
        return posts["posts"]

    def get_post(self, id):
        url = self.BASE_URL + '/sites/' + self.site + '/posts/' + id
        return self._http_get(url)

    def _http_get(self, url):
        r, c = self._http.request(url)
        c = json.loads(c)
        if c.get('status', '').lower() == "error" or "error" in c:
            raise WordPressException(c.get('error'))
        return c



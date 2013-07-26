"""
A WordPress client written in Python
"""
# Using the WordPress REST API https://public-api.wordpress.com/rest/v1
# See http://developer.wordpress.com/docs/api

__author__ = "Craig Cook (BoyCook)"
__version__ = "0.0.1"


class WordPress():
    BASE_URL = 'https://public-api.wordpress.com/rest/v1'

    def __init__(self, site):
        self.site = site

    def get_posts(self):
        print 'Getting posts'

    def get_post(self):
        print 'Getting post'



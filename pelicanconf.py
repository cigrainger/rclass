#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Christopher Grainger'
SITENAME = u'R for Energy Economics and Policy'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TYPOGRIFY= True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
RELATIVE_URLS = True

YEARNOW = '{date:%Y}'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

THEME = "/Users/cigrainger/Git/mockingbird-mod"

DISQUS_SITENAME = u'rforenergy'
GOOGLE_ANALYTICS = 'UA-47101624-1'

STATIC_PATHS = ['images', 'extra/CNAME', 'slides']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
PAGE_EXCLUDES = ['slides']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

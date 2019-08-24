#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aiyana'
SITENAME = "Aiyana Brooks"
SITEURL = 'https://aiyanabrooks.com'
FAVICON = 'images/favicon.png'

PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Theme settings
THEME = "themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'cerulean'  #try flatly if you get sick of cerulean
ABOUT_ME = "My name is Aiyana. I became a software engineer because I love solving puzzles and I love learning new things. We all wear many hats in this life. Some of the other hats I wear are mom, teacher, and student."
AVATAR = "images/profile.png"
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None



# Blogroll
LINKS = (('TESOL Portfolio', 'http://aiyanabrookstesol.strikingly.com/'),
         )

# Social widget
SOCIAL = (('github', 'https://github.com/ariesunique/'),
          ('linkedin', 'https://www.linkedin.com/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
LOAD_CONTENT_CACHE = True
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aiyana'
SITENAME = "Aiyana's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Theme settings
THEME = "themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'cerulean'
ABOUT_ME = "Here's a blurb about me. Bronx engineer, Aries, mom"
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}


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
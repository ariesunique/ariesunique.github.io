#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

###############################
#   MAIN SETTINGS
###############################

AUTHOR = 'Aiyana'
SITENAME = "Aiyana Brooks"
SITEURL = 'https://aiyanabrooks.com'
FAVICON = 'images/favicon.png'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


###############################
#   THEME SETTINGS
###############################

THEME = "themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'cerulean'  #try flatly if you get sick of cerulean

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'tag_cloud']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DISPLAY_PAGES_ON_MENU = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True  # this wills show the date on the main blog list
DEFAULT_PAGINATION = 10

DOCUTIL_CSS = True


###############################
#   SIDEBAR SETTINGS
###############################

#SIDEBAR_ON_LEFT = True
#PADDED_SINGLE_COLUMN_STYLE = True
ABOUT_ME = "My name is Aiyana. I became a software engineer because I love solving puzzles and I love learning new things. We all wear many hats in this life. Some of the other hats I wear are mom, teacher, and student."
#AVATAR = "images/penguin.jpg"

DISPLAY_TAGS_ON_SIDEBAR = True  # tag_cloud plugin must also be installed
DISPLAY_TAGS_INLINE = False
TAGS_URL = "tags.html"
    
    
###############################
#   FEED SETTINGS
###############################

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = False
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


###############################
#   LINKS
###############################

# Blogroll
LINKS = (('My TESOL Portfolio', 'http://aiyanabrookstesol.strikingly.com/'),
         )

# Social widgets
SOCIAL = (('github', 'https://github.com/ariesunique/'),
          ('bitbucket', 'https://bitbucket.org/ariesunique/'))



###############################
#   DEV SETTINGS (comment before committing)
###############################

#RELATIVE_URLS = True
#LOAD_CONTENT_CACHE = True

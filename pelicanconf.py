#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Gilson Filho'
SITENAME = 'Desbravando Django'
SITESUBTITLE = 'Experiências de quem procura ser perfeccionista com prazos'
SITEURL = 'http://localhost:8000'
DISQUS_SITENAME = 'desbravandodjango'
FACEBOOK_URL = ''

# Theme configurations
HEADER_COLOR = '#0c3c26'

PATH = 'content'
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Set the article URL
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/desbravandodjango'),
          ('Twitter', 'http://twitter.com/desbravandodjango'),)

DEFAULT_PAGINATION = 20

# STATIC_OUT_DIR requires pelican 3.3+.
STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']
NOTEBOOK_DIR = 'notebooks'

# Plugin configuration
PLUGIN_BASE = os.path.join(BASE_PATH, 'plugins')
PLUGIN_PATHS = [PLUGIN_BASE]
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.literal',
           'representative_image', 'liquid_tags.notebook']

# Theme configuration
THEME_PATH = os.path.join(BASE_PATH, 'themes')
THEME = os.path.join(THEME_PATH, 'desbravandodjango-theme')
FAVICON_NAME = 'favicon.ico'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# coding: utf-8
import os
import sys


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '_plugins'))

# Pelican settings (look at http://docs.getpelican.com/en/3.4.0/settings.html)

AUTHOR = 'Emil Infinite'
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'ru'
DISQUS_SITENAME = 'infinitegitcom'
GITHUB_URL = 'https://github.com/Infinite96'
PLUGINS = ['neighbors', 'multi_part', 'youtube']
RELATIVE_URLS = True
SITENAME = 'infinite96.github.io'
SITEURL = 'http://infinite96.github.io'
STATIC_PATHS = ['static']
THEME = '_theme'
TIMEZONE = 'Europe/Moscow'


GITHUB_IDENTIFICATOR = 'http://github.com/infinite96'

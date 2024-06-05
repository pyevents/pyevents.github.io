import os
import sys
from pelican import signals

sys.path.append(os.path.join(os.path.dirname(__file__), "plugins"))

import filters

AUTHOR = "Ali Tavallaie"
SITENAME = "PyEvents"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "fa"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 12
THEME = "themes/pyevents"
EXTRA_METADATA = {
    "signup_link": "signup_link",
    "original_link": "original_link",
    "poster": "poster",
}


# Prevent Pelican from generating individual article pages
ARTICLE_SAVE_AS = ""
ARTICLE_URL = ""
PAGE_SAVE_AS = ""
PAGE_URL = ""

# Generate tag pages
TAG_SAVE_AS = "tags/{slug}.html"
TAGS_SAVE_AS = "tags.html"

TEMPLATE_PAGES = {"404.html": "404.html"}
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Register the custom filter
filters.register()

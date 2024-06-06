import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://pyevents.github.io"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ["static", "images"]

EXTRA_PATH_METADATA = {
    "static/css/main.css": {"path": "static/css/main.css"},
    "static/images/default-poster.png": {"path": "static/images/default-poster.png"},
}

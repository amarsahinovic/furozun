#! /usr/bin/env python3
import sys
import os
from flask import Flask, render_template
from flask.ext.flatpages import FlatPages
from flask_frozen import Freezer

CWD = os.getcwd()
get_path = lambda * x: os.path.join(CWD, *x)

FUROZUN_CONFIG_FILENAME = '.furozun'
FUROZUN_CONFIG_FILE = get_path(CWD, FUROZUN_CONFIG_FILENAME)

# Don't do anything unless this is a content directory
if not os.path.isfile(FUROZUN_CONFIG_FILE):
    print("Missing .furozun file!", file=sys.stderr)
    sys.exit()

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

# Since this is used as an global app, we must configure the dirs manually
FLATPAGES_ROOT = get_path('pages')
FREEZER_DESTINATION = get_path('build')
FUROZUN_TEMPLATE_DIR = get_path('templates')
FUROZUN_STATIC_DIR = get_path('static')

app = Flask(__name__, 
            static_folder=FUROZUN_STATIC_DIR,
            template_folder=FUROZUN_TEMPLATE_DIR)

app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    # Pages with unlisted in meta are not show in listings
    # These are used for static pages like contact etc.
    listed_pages = (p for p in pages if 'unlisted' not in p.meta)
    return render_template('index.html', pages=listed_pages)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    # Use custom template if specified
    template = page.meta.get('template', 'page.html')
    return render_template(template, page=page)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)

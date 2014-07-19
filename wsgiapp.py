"""
This is a handler for running tiddlyweb under web servers that can be
configured to host an Python module as a WSGI application. Such servers
include apache2 using mod_wsgi, or nginx using uwsgi.
"""

import os
import sys

# you may wish to change this path
# It can also be controlled from mod_wsgi config.
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

def start():
    dirname = os.path.dirname(__file__)
    if sys.path[0] != dirname:
        sys.path.insert(0, dirname)
    from tiddlyweb.web import serve
    app = serve.load_app(app_prefix='', dirname=dirname)
    return app

# web server code will look for a callable named application
application = start()

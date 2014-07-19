import os

os.environ['PYTHON_EGG_CACHE'] = '/tmp'

def start():
    def app(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return ['Hello World']
    return app

# web server code will look for a callable named application
application = start()

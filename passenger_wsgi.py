import os
import sys
from testproject.wsgi import application

sys.path.insert(0, os.path.dirname(__file__))


# environ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")
def applications(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It Works!\n'
    version = 'Python %s\n' % sys.version.split()[0]
    response = '\n'.join([message, version])
    return [response.encode()]

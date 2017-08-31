
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

import web

import yaml

import app.configure
import app.insert
import app.media
import app.collection
import app.playlist

configuration = yaml.load(open('../config.yaml'))

if configuration['debugmode'] == True:
    print configuration

# Ensure directory configuration is valid
try:
    dc = app.configure.ConfigureDirectories()
    dc.configure(configuration['data'])
except:
    raise
    exit()

urls = (
    '/hello', 'hello',
    '/random', 'random',
    '/media', 'app.media.Media',
    '/collection', 'app.collection.Collection',
    '/info', 'info',
    '/playlist', 'app.playlist.Playlist'
    )

application = web.application(urls, globals()).wsgifunc()
application.root_path = os.path.dirname(os.path.abspath(__file__))


class hello:
    def GET(self):
        return configuration['hellostring']

class info:
    def GET(self):
        return configuration

class random:
    def GET(self):
        d = configuration['data']['dir'] + configuration['data']['audio']
        files = os.listdir(d)
        return "<a href='static/" +\
                configuration['data']['audio'] + files[0] +\
                "'>Link</a>"


#class shutdown:
#    def GET(self):
#        application.stop()
#        exit()
#        return 0

if __name__ == "__main__":
    application = web.application(urls, globals())
    application.run()


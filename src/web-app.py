
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

import web

import yaml

import app.configure
import app.insert
import app.media
import app.collection
import app.playlist
import app.initialize

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
    '/initialize', 'app.initialize.GetRandom',
    '/media', 'app.media.Media',
    '/info', 'app.info.GetInfo',
    )

application = web.application(urls, globals()).wsgifunc()
application.root_path = os.path.dirname(os.path.abspath(__file__))


class hello:
    def GET(self):
        return configuration['hellostring']



#class shutdown:
#    def GET(self):
#        application.stop()
#        exit()
#        return 0

if __name__ == "__main__":
    application = web.application(urls, globals())
    web.config.update({"configuration" : configuration})
    application.run()


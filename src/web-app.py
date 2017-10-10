
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

import web

import yaml

import app.configure
import app.initialize
import app.info
import app.recommend
import app.mir.metadata_extraction as meta

os.chdir(os.path.dirname(os.path.abspath(__file__)))
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
    '/info', 'app.info.GetInfo',
    '/info/(.+)', 'app.info.GetInfo',
    '/recommend', 'app.recommend.Recommend'
    )

application = web.application(urls, globals()).wsgifunc()
application.root_path = os.path.dirname(os.path.abspath(__file__))

class hello:
    def GET(self):
        return configuration['hellostring']


if __name__ == "__main__":
    application = web.application(urls, globals())
    web.config.update({"configuration" : configuration})

    MDB = meta.MacunaimaDBGenerator()
    MDB.operate_dir(True)

    application.run()


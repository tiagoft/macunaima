
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

import web
from web.contrib.template import render_jinja

import constants

#import app.db.id3tosql
import app.insert
import app.media
import app.collection
import app.playlist

urls = (
    '/shutdown', 'shutdown',
    '/hello', 'hello',
    '/media', 'app.media.Media',
    '/collection', 'app.collection.Collection',
    '/info', 'info',
    '/playlist', 'app.playlist.Playlist'
    )

application = web.application(urls, globals()).wsgifunc()
application.root_path = os.path.dirname(os.path.abspath(__file__))


render = render_jinja(
         os.path.dirname(__file__) + "/" + constants.template_directory,   # Set template directory.
         encoding = 'utf-8',                         # Encoding.
         )


class hello:
    def GET(self):
        p = app.insert.Insert(render)
        return p.GET(None)

class info:
    def GET(self):
        p = constants.dbfile + "<br>" + constants.files_directory
        return p


class shutdown:
    def GET(self):
        application.stop()
        exit()
        return 0

if __name__ == "__main__":
    application = web.application(urls, globals())
    application.run()


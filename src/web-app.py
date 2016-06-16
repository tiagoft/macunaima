
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

import web
from web.contrib.template import render_jinja

import constants

#import app.db.id3tosql
import app.insert
import app.media

urls = (
    '/shutdown', 'shutdown',
    '/hello', 'hello',
    '/media', 'app.media.Media',
    )

app_object = web.application(urls, globals())

render = render_jinja(
         constants.template_directory,   # Set template directory.
         encoding = 'utf-8',                         # Encoding.
         )


class hello:
    def GET(self):
        p = app.insert.Insert(render)
        return p.GET(None)



class shutdown:
    def GET(self):
        app_object.stop()
        exit()
        return 0


if __name__ == "__main__":
    app_object.run()


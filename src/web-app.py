import web
from web.contrib.template import render_jinja

import constants

#import app.db.id3tosql
import app.insert

urls = (
    '/(.*)', 'hello',

    )

app_object = web.application(urls, globals())

render = render_jinja(
         constants.template_directory,   # Set template directory.
         encoding = 'utf-8',                         # Encoding.
         )


class hello:
    def GET(self, name):
        if not name:
            name = 'World'
            return 'Hello, ' + name + '!'

        else:
            p = app.insert.Insert(render)
            return p.GET(None)
            #return render.information_table(name=name)


if __name__ == "__main__":
    app_object.run()


import web
import sqlite3
import os
import sys
from web.contrib.template import render_jinja

import constants

render = render_jinja(
         constants.mypath + "/" + constants.template_directory,   # Set template directory.
         encoding = 'utf-8',                         # Encoding.
         )


class Collection():
    def GET(self):
        query = "SELECT id, title, artist from MEDIA;"

        conn = sqlite3.connect(constants.dbfile)
        c = conn.cursor()
        data = []
        for d in c.execute(query):
            data.append({'title': d[1], 'artist': d[2], 'id': d[0]})

        conn.commit()

        print data

        return render.collection_view(media_elements = data)
#        ret = ""
#        for row in c.execute(query):
#            ret += str(row)
#
#        return ret


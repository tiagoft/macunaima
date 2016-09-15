import web
import sqlite3
import os
import sys
from web.contrib.template import render_jinja
import json

import constants
import playlist

render = render_jinja(
         constants.mypath + "/" + constants.template_directory,   # Set template directory.
         encoding = 'utf-8',                         # Encoding.
         )


class Collection():
    def GET(self):
        data = playlist.Playlist().GET()
        data = json.loads(data)

        web.header('Content-Type', 'text/HTML')
        return render.collection_view(media_elements = data)
#        ret = ""
#        for row in c.execute(query):
#            ret += str(row)
#
#        return ret


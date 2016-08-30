import web
import sqlite3
import os
import sys
from web.contrib.template import render_jinja
import json

import constants

render = render_jinja(
         constants.mypath + "/" + constants.template_directory,   # Set template directory.
         encoding = 'utf-8',                         # Encoding.
         )


class Playlist():
    def get_json(self, method='NEW'):
        if method == 'NEW':
            query = "SELECT id, title, artist from MEDIA ORDER BY id DESC;"
        elif method == 'RAND':
            query = "SELECT id, title, artist from MEDIA ORDER BY RANDOM();"
        else:
            return None

        conn = sqlite3.connect(constants.dbfile)
        c = conn.cursor()
        json_data = []
        for d in c.execute(query):
            json_data.append({'title': d[1], 'artist': d[2], 'id': d[0]})

        conn.commit()

        json_data = json.dumps(json_data)

        return json_data


    def GET(self):
        # Select method (default = NEW)
        data = web.input()

        if 'method' not in data:
            method = 'NEW'
        else:
            method = data['method']

        return self.get_json(method)

#        ret = ""
#        for row in c.execute(query):
#            ret += str(row)
#
#        return ret



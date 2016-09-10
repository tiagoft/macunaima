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
    def get_json(self, method='NEW', offset=0, limit=10, reject=None,

            accept_only=None):

        str_accept = ""
        str_rejection = ""
        if reject is not None:
            str_rejection = " where id not in ("
            for r in reject:
                str_rejection += str(r) + ", "
            str_rejection += "-1) "
        elif accept_only is not None:
            str_accept = " where id in ("
            for r in accept_only:
                str_accept += str(r) + ", "
            str_accept += "-1) "

        if method == 'NEW':
            str_sort = " ORDER BY id DESC "
        elif method == 'RAND':
            str_sort = " ORDER BY RANDOM() "
        else:
            return None

        str_limits = " LIMIT " + str(limit) + " OFFSET " + str(offset) + " "

        query = "SELECT id, title, artist from MEDIA" + str_rejection\
                    + str_accept + str_sort + str_limits + ";"

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

        if 'reject' in data:
            data0 = web.input(reject=[])
            rejection = data0.reject
        else:
            rejection = None

        if 'accept' in data:
            data0 = web.input(accept=[])
            accept = data0.accept
        else:
            accept= None

        if 'offset' in data:
            offset = data['offset']
        else:
            offset = 0

        if 'limit' in data:
            limit = data['limit']
        else:
            limit = 10


        return self.get_json(method, reject=rejection, accept_only=accept,
                offset=offset, limit=limit)

#        ret = ""
#        for row in c.execute(query):
#            ret += str(row)
#
#        return ret



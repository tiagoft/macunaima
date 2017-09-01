import json
import os
import random
import web

import session

class GetInfo:
    def __init__(self):
        pass

    def GET(self):
        try:
            json_data = json.loads(web.data())
            data = json.JSONDecoder.decode(json_data)
            primary_key = data['session_id']
        except:
            primary_key = None

        elements = session.SessionDB().retrieve(primary_key)
        enc = json.JSONEncoder().encode(elements)
        return enc


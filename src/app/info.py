import json
import os
import random
import web

import session

class GetInfo:
    def __init__(self):
        pass

    def GET(self, args=None):
        if args is not None:
            primary_key = args
        else:
            primary_key = None

        print primary_key

        elements = session.SessionDB().retrieve(primary_key)
        enc = json.JSONEncoder().encode(elements)
        return enc


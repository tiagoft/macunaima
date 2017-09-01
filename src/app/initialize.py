import uuid
import json
import os
import random
import web

import session

class GetRandom:
    def __init__(self):
        pass

    def GET(self):
        configuration = web.config.configuration
        data = self._generate_random(configuration)
        enc = json.JSONEncoder()
        js_out = enc.encode(data)

        session.SessionDB().insert(js_out)

        return enc.encode(js_out)

    def _generate_random(self, configuration):
        d = configuration['data']['dir'] + configuration['data']['audio']
        files = os.listdir(d)
        random.shuffle(files)

        session_id = uuid.uuid4().hex

        data = {'session_id': session_id,
                'recommendation': 'static/' + configuration['data']['audio'] +\
                        files[0]}

        return data

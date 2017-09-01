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
        session.SessionDB().insert(data)

        return enc.encode(data)

    def _generate_random(self, configuration):
        d = configuration['data']['dir'] + configuration['data']['audio']
        files = os.listdir(d)
        random.shuffle(files)

        session_id = uuid.uuid4().hex

        data = {'session_id': session_id,
                'response': 'init',
                'recommendation': 'static/' + configuration['data']['audio'] +\
                        files[0]}

        return data

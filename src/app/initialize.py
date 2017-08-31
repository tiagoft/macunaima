import hashlib
import json
import os
import random
import web


class GetRandom:
    def __init__(self):
        pass

    def GET(self):
        configuration = web.config.configuration
        data = self._generate_random(configuration)
        enc = json.JSONEncoder()
        return enc.encode(data)

    def _generate_random(self, configuration):
        d = configuration['data']['dir'] + configuration['data']['audio']
        files = os.listdir(d)
        random.shuffle(files)

        session_id = hashlib.md5().hexdigest()

        data = {'session_id': session_id,
                'recommendation': 'static/' + configuration['data']['audio'] +\
                        files[0]}

        return data

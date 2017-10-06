import uuid
import json
import os
import random
import web

import engines
import session


class GetRandom:
    def __init__(self):
        pass

    def GET(self):
        configuration = web.config.configuration
        data = self._generate_coldstart(configuration)
        enc = json.JSONEncoder()
        session.SessionDB().insert(data)
        web.header('Content-Type', 'application/json')
        return enc.encode(data)

    def _generate_coldstart(self, configuration):
        d = configuration['data']['dir'] + configuration['data']['audio']

        random_selector = random.random()
        print random_selector
        if random_selector > 0.5:
            rec = engines.Dummy('static/' + configuration['data']['audio'])
            engine = 'dummy'
        else:
            rec = engines.Explorer('static/' + configuration['data']['audio'])
            engine = 'exporer'

        recommendation = rec.retrieve([])

        session_id = uuid.uuid4().hex

        data = {'session_id': session_id,
                'response': 'init',
                'recommendation': 'static/' + configuration['data']['audio'] +\
                        recommendation,
                'engine': engine}

        return data

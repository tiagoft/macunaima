import json
import session
import time
import web

import engines.dummy

class Recommend:
    def __init__(self):
        pass

    def GET(self, action, session_id, media_file):
        configuration = web.config.configuration
        s = session.SessionDB()

        interaction_data = {'session_id': session_id,
                'action': action,
                'file': media_file,
                'timestamp': time.time()}

        print interaction_data

        history = s.retrieve(session_id)
        history.append(interaction_data)

        # TODO: recommendation system goes here!
        rec = engines.dummy.Dummy('static/' + configuration['data']['audio'])
        recommendation = rec.retrieve(history)

        response_data = {'session_id': session_id,
                'response': 'recommend',
                'recommendation': recommendation}

        print response_data

        s.insert(interaction_data)
        s.insert(response_data)

        web.header('Content-Type', 'application/json')
        enc = json.JSONEncoder()
        return enc.encode(response_data)

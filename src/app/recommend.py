import json
import session
import time
import web

import engines.dummy

class Recommend:
    def __init__(self):
        pass

    def POST(self):
        configuration = web.config.configuration
        s = session.SessionDB()

        print web.data()

        post_data = json.loads(web.data())


        interaction_data = {'session_id': str(post_data['session_id']),
                'action': str(post_data['action']),
                'file': str(post_data['media_file']),
                'timestamp': time.time()}

        print interaction_data

        history = s.retrieve(interaction_data['session_id'])
        history.append(interaction_data)

        # TODO: recommendation system goes here!
        rec = engines.dummy.Dummy('static/' + configuration['data']['audio'])
        recommendation = rec.retrieve(history)

        response_data = {'session_id': interaction_data['session_id'],
                'response': 'recommend',
                'recommendation': recommendation}


        s.insert(interaction_data)
        s.insert(response_data)

        web.header('Content-Type', 'application/json')
        enc = json.JSONEncoder()
        return enc.encode(response_data)

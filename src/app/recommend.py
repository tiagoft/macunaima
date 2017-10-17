import json
import session
import time
import web

import engines

class Recommend:
    def __init__(self):
        pass

    def POST(self):
        configuration = web.config.configuration
        s = session.SessionDB()
        web.header('Content-Type', 'application/json')
        enc = json.JSONEncoder()

        #print web.data()

        post_data = json.loads(web.data())

        interaction_data = {'session_id': str(post_data['session_id']),
                'action': str(post_data['action']),
                'file': str(post_data['media_file']),
                'timestamp': time.time()}

        s.insert(interaction_data)
        #print "Received interaction:", interaction_data

        history = s.retrieve(interaction_data['session_id'])
        #history.append(interaction_data)

        for h in history:
            if 'action' in h.keys():
                print h['action']
            else:
                print h

        # TODO: recommendation system goes here!
        # Recommendation system selector (TODO: can I do this without hardcoding
        # the recommendation systems?)
        if interaction_data['action'] == 'skip':
            init_data = s.retrieve_init(interaction_data['session_id'])
            if str(init_data['engine']) == 'dummy':
                rec = engines.Dummy('static/' + configuration['data']['audio'])
            elif str(init_data['engine']) == 'explorer':
                rec = engines.Explorer('static/' + configuration['data']['audio'])

            # Recommender system operation
            recommendation = rec.retrieve(history)

            response_data = {'session_id': str(interaction_data['session_id']),
                'response': str('recommend'),
                'recommendation': str(recommendation)}

            s.insert(response_data)


            web.header('Content-Type', 'application/json')
            enc = json.JSONEncoder()
            return enc.encode(response_data)

        else:
            return enc.encode(interaction_data)

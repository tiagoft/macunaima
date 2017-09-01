import time
import tinydb
import json
import web

class SessionDB:
    def __init__(self):
        pass

    def insert(self, json_params):
        """Inserts a new interaction into the SessionDB
        """

        params = json.JSONDecoder().decode(json_params)

        if 'timestamp' not in params.keys():
            params['timestamp'] = time.time()

        json_params = json.JSONEncoder().encode(params)

        db = tinydb.TinyDB(self._dbpath())
        db.insert(params)
        return True

    def retrieve(self, primary_key):
        """Gets all interactions for a primary_key
        """
        db = tinydb.TinyDB(self._dbpath())
        query = tinydb.Query()
        if primary_key is not None:
            ret = db.search(query.session_id == primary_key)
        else:
            ret = db.all()

        st = sorted(ret, key=lambda k: k['timestamp'])
        return st

    def _dbpath(self):
        configuration = web.config.configuration
        d = configuration['data']['dir'] + configuration['data']['user']
        sessiondb = 'session.db'
        dbpath = d + sessiondb
        return dbpath


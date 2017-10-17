import time
import tinydb
import json
import web

class SessionDB:
    def __init__(self):
        pass

    def insert(self, params):
        """Inserts a new interaction into the SessionDB
        """

        if 'timestamp' not in params.keys():
            params['timestamp'] = time.time()

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

    def retrieve_init(self, primary_key):
        """Gets the initial for a primary_key
        """
        db = tinydb.TinyDB(self._dbpath())
        query = tinydb.Query()
        if primary_key is not None:
            ret = db.search((query.session_id == primary_key) &\
                            (query.response == 'init'))
        else:
            return None

        return ret[0]


    def _dbpath(self):
        configuration = web.config.configuration
        d = configuration['data']['dir'] + configuration['data']['user']
        sessiondb = 'session.db'
        dbpath = d + sessiondb
        return dbpath


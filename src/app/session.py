import time
import tinydb
import web

class SessionDB:
    def __init__(self):
        pass

    def insert(self, params):
        """Inserts a new interaction into the SessionDB
        """
        if 'timestamp' not in params.keys():
            params['timestamp'] = time.time()

        db.insert(params)
        return True

    def get(self, primary_key):
        """Gets all interactions for a primary_key
        """
        db = tinydb.TinyDB(self._dbpath())

    def _dbpath(self):
        configuration = web.config.configuration
        d = configuration['data']['dir'] + configuration['data']['user']
        sessiondb = 'session.db'
        dbpath = d + sessiondb



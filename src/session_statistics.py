import time
import tinydb
import sys
import numpy as np

class SessionDB:
    def __init__(self, dbpath):
        self._dbpath = dbpath

    def retrieve(self, primary_key):
        """Gets all interactions for a primary_key
        """
        db = tinydb.TinyDB(self._dbpath)
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
        db = tinydb.TinyDB(self._dbpath)
        query = tinydb.Query()
        if primary_key is not None:
            ret = db.search((query.session_id == primary_key) &\
                            (query.response == 'init'))[0]
        else:
            ret = db.search(query.response == 'init')

        return ret

class SessionStats:
    def __init__(self, sessiondb):
        self._SessionDB = sessiondb

    def number_of_songs(self, primary_key):
        data = self._SessionDB.retrieve(primary_key)
        nsongs = len([d for d in data if 'recommendation' in d.keys()])
        return nsongs

    def number_of_likes(self, primary_key):
        data = self._SessionDB.retrieve(primary_key)
        nlikes = len([d for d in data if 'action' in d.keys() and\
                d['action']=='like'])
        return nlikes

    def interaction_time(self, primary_key):
        data = self._SessionDB.retrieve(primary_key)
        if len(data)==1:
                return 0.0
        t0 = float(data[0]['timestamp'])
        t1 = float(data[-1]['timestamp'])
        return t1-t0

    def fraction_of_likes(self, primary_key):
        data = self._SessionDB.retrieve(primary_key)
        nlikes = len([d for d in data if 'action' in d.keys() and\
                d['action']=='like'])
        nsongs = len([d for d in data if 'recommendation' in d.keys()])
        return float(nlikes)/float(nsongs)



def stats(sessions, verbose=1):
    all_sessions = []
    st = SessionStats(db)
    for s in sessions:
        key = s['session_id']
        session_data = [st.number_of_songs(key),
                        st.number_of_likes(key),
                        st.interaction_time(key),
                        st.fraction_of_likes(key)]
        all_sessions.append(session_data)
    all_sessions_np = np.array(all_sessions)
    avg = np.average(all_sessions_np, axis=0)
    std = np.std(all_sessions_np, axis=0)

    if verbose == 1:
        for i in xrange(len(avg)):
            print "Measure " + str(i) + ": " + str(avg[i]) + " \\pm " + str(std[i])
    return avg, std

if __name__ == "__main__":
    dbpath = sys.argv[1]
    db = SessionDB(dbpath)

    print "Sessions:"
    ret = db.retrieve_init(None)
    print "Found:", len(ret), " sessions"

    # Separate explorer from dummy engines
    explorer_sessions = [e for e in ret if 'engine' in e.keys() and\
            e['engine'] == 'explorer']
    dummy_sessions = [e for e in ret if 'engine' in e.keys() and\
            e['engine'] == 'dummy']

    print "Explorer:", len(explorer_sessions)
    print "Dummy:", len(dummy_sessions)

    print "Statistics: number of songs, number of likes, interaction time,\
        fraction_of_likes"

    print "Explorer statistics:"
    stats(explorer_sessions)
    print "Dummy statistics:"
    stats(dummy_sessions)

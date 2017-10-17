import numpy as np
import tinydb
import os
import web
import time

import extract_features

class SingleFileMetadataDBGenerator:
    def __init__(self, dbpath):
        self.dbpath = dbpath
        pass

    def insert_db(self, audiofile):
        data = self.retrieve(audiofile)

        if len(data) > 0:
            return

        feat = extract_features.features(audiofile)
        self.insert(feat)

    def insert(self, params):
        """Inserts a new entry into the DB
        """

        if 'timestamp' not in params.keys():
            params['timestamp'] = time.time()

        db = tinydb.TinyDB(self.dbpath)
        db.insert(params)
        return True

    def retrieve(self, primary_key):
        """Gets entries related to files
        """
        db = tinydb.TinyDB(self.dbpath)
        query = tinydb.Query()
        if primary_key is not None:
            pkey = primary_key.replace('static', '../data')
            ret = db.search(query.filename == pkey)
        else:
            ret = db.all()

        return ret

    def rnear_retrieve(self, target_vector, restricted_keys):
        ret = self.retrieve(None)
        print "rnear_retrieve"
        print target_vector

        best_distance = 9999999999999
        best_key = None
        for entry in ret:
            if entry['filename'].replace('../data', 'static') not in restricted_keys:
                this_vector = np.array(entry['features'])
                this_distance = np.sum( (this_vector - target_vector)**2 )
                if this_distance < best_distance:
                    best_key = entry['filename'].replace('../data', 'static')
                    best_distance = this_distance

        return best_key


class MacunaimaDBGenerator:
    def __init__(self):
        pass

    def operate_dir(self, verbose=False):
        d = DBPath()
        audiopath = d._audiopath()
        dbpath = d._dbpath()
        all_files = [audiopath + i \
                for i in os.listdir(audiopath)]

        DBmanager = SingleFileMetadataDBGenerator(dbpath)

        for f in all_files:
            DBmanager.insert_db(f)
            if verbose == True:
                print f

        return True


class DBPath:
    def __init__(self):
        pass

    def _audiopath(self):
        configuration = web.config.configuration
        d = configuration['data']['dir'] + configuration['data']['audio']
        return d

    def _dbpath(self):
        configuration = web.config.configuration
        d = configuration['data']['dir'] + configuration['data']['meta']
        metadatadb = configuration['search']['featureset'] + '.db'
        dbpath = d + metadatadb
        return dbpath



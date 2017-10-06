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
            ret = db.search(query.filename == primary_key)
        else:
            ret = db.all()

        return ret

class MacunaimaDBGenerator:
    def __init__(self):
        pass

    def operate_dir(self, verbose=False):
        audiopath = self._audiopath()
        dbpath = self._dbpath()
        all_files = [audiopath + i \
                for i in os.listdir(audiopath)]

        DBmanager = SingleFileMetadataDBGenerator(dbpath)

        for f in all_files:
            DBmanager.insert_db(f)
            if verbose == True:
                print f

        return True

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





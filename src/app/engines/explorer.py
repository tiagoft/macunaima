import numpy as np
import os
import random

import engine
import app.mir.metadata_extraction as meta



class Explorer(engine.Engine):


    def retrieve(self, history):
        print "Explorer Engine!"

        used_files = [a['file'] for a in history if 'file' in a.keys()]

        dbpath = meta.DBPath()._dbpath()
        metadb = meta.SingleFileMetadataDBGenerator(dbpath)

        # a0 = status of last track; a1 = status of 2nd last track
        a0, a1 = self._last_tracks_status(history)


        if a0 == False and a1 == False:
            print "Random recommendation! (F F)"
            all_files = \
                [self.audiodb_path + i \
                    for i in os.listdir(self.audiodb_path)]

            allowed_files = [i for i in all_files if i not in used_files]

            if len(allowed_files)==0:
                return used_files[-1]
            else:
                return random.choice(allowed_files)

        filt_hist = [h['recommendation'] for h in history\
                if 'recommendation' in h.keys()]
        d0 = self._get_vector(metadb, filt_hist, -1)
        d1 = self._get_vector(metadb, filt_hist, -2)

        # Recommendation goes here!

        rec = self._recommend(metadb, d0, d1, a0, a1, filt_hist)
        if rec is None:
            print "Random recommendation! (F F)"
            all_files = \
                [self.audiodb_path + i \
                    for i in os.listdir(self.audiodb_path)]

            allowed_files = [i for i in all_files if i not in used_files]

            if len(allowed_files)==0:
                return used_files[-1]
            else:
                return random.choice(allowed_files)
        else:
            return rec


    def _recommend(self, metadb, d0, d1, a0, a1, filt_hist):
        print np.array(d0[0]['features'])
        n0 = np.array(d0[0]['features'])

        if (type(d1) is list) and (len(d1) > 0):
            print np.array(d1[0]['features'])
            n1 = np.array(d1[0]['features'])
        else:
            n1 = False

        next_mean = self._explore(n0, n1, a0, a1)

        print n0
        print n1
        print next_mean
        db = meta.SingleFileMetadataDBGenerator(meta.DBPath()._dbpath())
        ret = db.rnear_retrieve(next_mean, filt_hist)

        return ret


    def _explore(self, d0, d1, a0, a1):
        """Gets next position
        """
        # Case 1: only one like
        if type(d1) is bool:
            if a0 == True:
                return d0

        if a0 == False and a1 == True:
            return d1

        if a0 == True and a1 == True:
            return (d0+d1)/2.0

        if a0 == True and a1 == False:
            return d0



    def _get_vector(self, metadb, filt, idx=-1):
        """Returns feature vector for element with history idx
        """
        try:
            key = filt[idx]
            data = metadb.retrieve(key)
            return data

        except IndexError:
            return False




    def _split_positives_negatives(self, history):
        pos = [str(k['file']) for k in history if 'action' in k.keys() and k['action']=='like']
        neg = [str(k['file']) for k in history if 'action' in k.keys() and k['action']=='skip']
        return pos, neg


    def _like_track_at(self, history, idx=-1):
        try:
            if 'action' in history[idx].keys() and history[idx]['action']=='skip':
                if 'action' in history[idx-1].keys() and history[idx-1]['action']=='like':
                    return True
            return False

        except IndexError:
            return False


    def _last_tracks_status(self, history):

        like_last = self._like_track_at(history, -1)
        if like_last == True:
            like_2last = self._like_track_at(history, -4)
        else:
            like_2last = self._like_track_at(history, -3)

        return like_last, like_2last


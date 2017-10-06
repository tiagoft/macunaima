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

        if a0 == False and a1 == True:
            print "False True"

        if a0 == True and a1 == True:
            print "True True"

        if a0 == True and a1 == False:
            print "True False!"



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


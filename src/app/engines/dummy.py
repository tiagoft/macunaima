import random
import os

import engine

class Dummy(engine.Engine):
    def _retrieve(self, positives, negatives):
        print "dummy engine!"
        allowed_files = \
            [self.audiodb_path + i \
                for i in os.listdir(self.audiodb_path)]



        filtered_files = [a for a in allowed_files\
                            if a not in (positives+negatives)]

        if len(filtered_files)==0:
            return random.choice(allowed_files[0])
        else:
            return filtered_files[0]


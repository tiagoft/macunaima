import os
import engine

class Dummy(engine.Engine):
    def _retrieve(self, positives, negatives):
        allowed_files = \
            [self.audiodb_path + i \
                for i in os.listdir(self.audiodb_path)]

        print positives
        print negatives
        filtered_files = [a for a in allowed_files\
                            if a.split('/')[-1] not in (positives+negatives)]

        if len(filtered_files)==0:
            return allowed_files[0]
        else:
            return filtered_files[0]


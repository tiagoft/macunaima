import os
import engine

class Dummy(engine.Engine):
    def _retrieve(self, positives, negatives):
        allowed_files = \
            [self.audiodb_path + i \
                for i in os.listdir(self.audiodb_path)]


        print positives
        print negatives
        print allowed_files
        print positives + negatives

        filtered_files = [a for a in allowed_files\
                            if a not in (positives+negatives)]

        print filtered_files
        if len(filtered_files)==0:
            return allowed_files[0]
        else:
            return filtered_files[0]


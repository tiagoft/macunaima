import os
import engine

class Dummy(engine.Engine):
    def _retrieve(self, positives, negatives):
        allowed_files = \
            ['static/' + self.audiodb_path + i \
                for i in os.listdir(self.audiodb_path)]

        filtered_files = [a for a in allowed_files\
                            if a not in (positives+negatives)]

        return filtered_files[0]

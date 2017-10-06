import os
import engine

class Explorer(engine.Engine):

    def retrieve(self, history):
        print "Explorer Engine!"
        allowed_files = \
            [self.audiodb_path + i \
                for i in os.listdir(self.audiodb_path)]


        print allowed_files

        filtered_files = [a for a in allowed_files\
                            if a not in (history)]

        print filtered_files
        if len(filtered_files)==0:
            return allowed_files[0]
        else:
            return filtered_files[0]


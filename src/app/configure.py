# Configure directories

import os

class ConfigureDirectories:
    def __init__(self):
        pass

    def configure(self, params):
        """Configure directories

        Params is a dictionary containing the following members:
        'dir' - the root directory for data
        'audio', 'meta', 'user' - data directories for specific uses

        Returns:
        True: in case of success
        Other: the error code, in case of errors
        """
        wd = os.getcwd()

        audiodir = wd + "/" +  params['dir'] + params['audio']
        metadir = wd + "/" +  params['dir'] + params['meta']
        userdir = wd + "/" + params['dir'] + params['user']

        self._statdir(audiodir)
        self._statdir(metadir)
        self._statdir(userdir)

        self._statlink(audiodir, wd + '/static/' + params['audio'])
        return True

    def _statdir(self, path):
        if os.path.exists(path) == False:
            try:
                os.makedirs(path)
            except:
                raise
        return True

    def _statlink(self, target, path):
        if os.path.exists(target) == False:
            return False
        if os.path.exists(path) == False:
            try:
                print target
                print path
                os.symlink(target, path.rstrip('/'))
            except:
                raise
        return True

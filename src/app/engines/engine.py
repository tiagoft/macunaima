
class Engine:
    def __init__(self, audiodb_path):
        self.audiodb_path = audiodb_path

    def retrieve(self, history):
        pos, neg = self._split_positives_negatives(history)
        return self._retrieve(pos, neg)


    def _retrieve(self, positives, negatives):
        raise NotImplementedError

    def _split_positives_negatives(self, history):
        pos = [k for k in history if 'action' in k.keys() and k['action']=='like']
        neg = [k for k in history if 'action' in k.keys() and k['action']=='skip']
        return pos, neg


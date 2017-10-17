
import sklearn.preprocessing as preprocessing
import numpy as np

class RecommendNearest():
    """Recommendation based on nearest neighbors"""

    def __init__(self):
        pass

    def recommend(self, dataset, likes, dislikes, skips):
        scaler = preprocessing.StandardScaler().fit_transform(dataset.data)
        lin, col = dataset.data.shape
        min_dist = 999999999999999999999999
        min_label = -1

        if likes is None:
            likes = []
        if dislikes is None:
            dislikes = []
        if skips is None:
            skips = []

        #print likes, dislikes, skips

        for i in xrange(lin):
            if (str(dataset.labels[i]) not in likes) and \
               (str(dataset.labels[i]) not in dislikes) and \
               (str(dataset.labels[i]) not in skips):
                analysis = dataset.data[i,:]
                for j in xrange(len(likes)):
                    ref = dataset.data[dataset.labels.index(int(likes[j])),:]
                    dist = np.linalg.norm(analysis-ref)
                    if dist < min_dist:
                        min_dist = dist
                        min_label = dataset.labels[i]

        return min_label





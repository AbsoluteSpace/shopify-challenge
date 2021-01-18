import numpy as np
from scipy import stats
import utils

class KNN:

    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X = X
        self.y = y 

    def predict(self, Xtest):
        X = self.X
        y = self.y
        n = X.shape[0]
        t = Xtest.shape[0]
        k = min(self.k, n)

        dist2 = utils.euclidean_dist_squared(X, Xtest)

        inds = np.argsort(dist2[:,0])
        return y[inds[:k]][1:]
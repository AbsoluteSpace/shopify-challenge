import os.path
import numpy as np

def euclidean_dist_squared(X, Xtest):
 
    return np.sum(X**2, axis=1)[:,None] + np.sum(Xtest**2, axis=1)[None] - 2 * np.dot(X,Xtest.T)
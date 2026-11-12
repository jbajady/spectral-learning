import numpy as np


class SVD:
    def __init__(self, n_components):
        self.n_components = n_components
        self.U = None
        self.S = None
        self.Vt = None

    def fit(self, X):
        # Perform Singular Value Decomposition
        U, S, Vt = np.linalg.svd(X, full_matrices=False)
        self.U = U[:, :self.n_components]
        self.S = S[:self.n_components]
        self.Vt = Vt[:self.n_components, :]

    def transform(self, X):
        # Project the data onto the lower-dimensional space
        return np.dot(X, self.Vt.T)

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
    
    def evaluation_variance_explained(self):
        # Calculate the variance explained by each singular value
        total_variance = np.sum(self.S ** 2)
        explained_variance = (self.S ** 2) / total_variance
        return explained_variance


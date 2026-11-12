import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        # Center the data
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        # Compute covariance matrix
        cov_matrix = np.cov(X_centered, rowvar=False)
        
        # Compute eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        
        # Sort eigenvalues and corresponding eigenvectors in descending order
        sorted_indices = np.argsort(eigenvalues)[::-1]
        sorted_eigenvalues = eigenvalues[sorted_indices]
        sorted_eigenvectors = eigenvectors[:, sorted_indices]
        
        # Select the top n_components
        self.components = sorted_eigenvectors[:, :self.n_components]

    def transform(self, X):
        X_centered = X - self.mean
        
        # Project the data onto the principal components
        return np.dot(X_centered, self.components)

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

    
    def evaluation_variance_explained(self, X):
        # Center the data
        X_centered = X - self.mean
        
        # Compute covariance matrix
        cov_matrix = np.cov(X_centered, rowvar=False)
        
        # Compute eigenvalues
        eigenvalues, _ = np.linalg.eigh(cov_matrix)
        
        # Sort eigenvalues in descending order
        sorted_eigenvalues = np.sort(eigenvalues)[::-1]
        
        # Calculate the variance explained by each principal component
        total_variance = np.sum(sorted_eigenvalues)
        explained_variance = sorted_eigenvalues / total_variance
        
        return explained_variance[:self.n_components]
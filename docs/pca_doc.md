# Principale Component Analysis (PCA)


    is algorithme  unsupervised machine learning and staticl method used reduce the complextitey(dimensionality) of high-dimensional datasets while retaining
    as much critical information (variance) as possible.

* The primary goals of PCA are:
  - Dimensionality reduction
  - Feature extraction
  - Data visualization
  - Noise reduction

## how to work  (PCA)

### mathematical foundations
   to understand PCA , we need to grasp a few key mathematical concepts:

1. Variance and Covariance
    Variance measures the spread of a single variable, while covariance measures the relationship between two variables.

    For a dataset X with n features, the covariance matrix C is defined as:
      ```
      varaince = sum(x-mean)^2/n-1

      C = (1 / (n-1)) * (X — μ)^T * (X — μ)
      ```
      Where μ is the mean vector of X.
  
 2. Eigenvectors and Eigenvalues
    For a square matrix A, if there exists a vector v and a scalar λ such that:
      ```
        Av = λv
      ```
    Then v is called an eigenvector of A, and λ is the corresponding eigenvalue.

  3. Singular Value Decomposition (SVD)
      SVD is a matrix factorization method that decomposes a matrix X into three matrices:
       ``` 
        X = UΣV^T
      ```
      Where U and V are orthogonal matrices, and Σ is a diagonal matrix of singular values.
### The PCA Algorithm
    the PCA algorithm can be broken down into the following steps:
    - standardize the dataset
    - compute the covariance matrix 
    - calculate eigenvalue an eigenvectors of covariance matrix 
    - sort k eigenvectors as the new features
    - transform the original dataset
### PCA from scratch

```

import numpy as np


def eigenvalues_eigenvectors(cov_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    idx = eigenvalues.argsort()[::-1]

    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    return eigenvalues, eigenvectors


def calculate_covariance(x):
    return np.cov(x, ddof=1)


def select_best_features(eigenvectors, n_components):
    k_eigenvectors = eigenvectors[:, :n_components]
    return k_eigenvectors


def pca_model(x, k_eigenvectors):
    return np.dot(k_eigenvectors.T, x)


if __name__ == "__main__":
    x = [1, 3, 5]
    y = [2, 4, 9]

    data = np.array([x, y])

    covariance_matrix = calculate_covariance(data)

    eigenvalues, eigenvectors = eigenvalues_eigenvectors(
        covariance_matrix
    )

    k_eigenvectors = select_best_features(eigenvectors, 1)

    print("Covariance Matrix:")
    print(covariance_matrix)

    print("Eigenvalues:")
    print(eigenvalues)

    print("Selected Eigenvectors:")
    print(k_eigenvectors)

    print("PCA Result:")
    print(pca_model(data, k_eigenvectors))
```
### PCA using scikit-learn 
  ```
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import load_iris
    import matplotlib.pyplot as plt


    iris = load_iris()
    X = iris.data
    y = iris.target

    scaler=StandardScaler()
    X_std = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    X_pca_sklearn = pca.fit_transform(X_std)
    print(y)

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X_pca_sklearn[:, 0], X_pca_sklearn[:, 1], c=y, cmap='viridis')
    plt.colorbar(scatter)
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.title('PCA of Iris Dataset (scikit-learn)')
    plt.show()
  ```

 ### Advantages:
   - Reduces dimensionality of the data
   - Removes correlated features
   - Improves algorithm performance
   - Helpful for data visualization
### Limitations:
   - Assumes linearity
   - Sensitive to feature scaling
   - May lose some interpretability
   - Not suitable for all types of data
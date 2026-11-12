from matplotlib import pyplot as plt

def visualize_svd(X, svd_model):

    # Project the data onto the lower-dimensional space
    X_transformed = svd_model.transform(X)

    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Plot the original data
    axes[0].scatter(X[:, 0], X[:, 1], alpha=0.5)
    axes[0].set_title('Original Data')
    axes[0].set_xlabel('Feature 1')
    axes[0].set_ylabel('Feature 2')

    # Plot the transformed data
    axes[1].scatter(X_transformed[:, 0], X_transformed[:, 1], alpha=0.5, color='orange')
    axes[1].set_title('Transformed Data (SVD)')
    axes[1].set_xlabel('Component 1')
    axes[1].set_ylabel('Component 2')

    plt.tight_layout()
    plt.show()


def visualize_pca(X, pca_model):

    # Project the data onto the lower-dimensional space
    X_transformed = pca_model.transform(X)

    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Plot the original data
    axes[0].scatter(X[:, 0], X[:, 1], alpha=0.5)
    axes[0].set_title('Original Data')
    axes[0].set_xlabel('Feature 1')
    axes[0].set_ylabel('Feature 2')

    # Plot the transformed data
    axes[1].scatter(X_transformed[:, 0], X_transformed[:, 1], alpha=0.5, color='green')
    axes[1].set_title('Transformed Data (PCA)')
    axes[1].set_xlabel('Component 1')
    axes[1].set_ylabel('Component 2')

    plt.tight_layout()
    plt.show()
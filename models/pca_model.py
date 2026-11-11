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


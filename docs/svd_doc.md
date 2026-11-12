# Singular Value Decomposition (SVD)

Singular Value Decomposition (SVD) is a factorization method in linear algebra that decomposes a matrix into three other matrices, providing a way to represent data in terms of its singular values.

SVD helps you splite that into three parts:
  - U: This part tells you about the people (like their general preferences).
  - Σ: This part shows how important each factor is (how much each rating matters).
  - Vᵀ: This part tells you about the products (how similar they are to each other)
Mathematically, the SVD of a matrix A (of size m×n) is represented as: A=UΣV^T
 
## how to perform singular value decomposition 

 To perform Singular Value Decomposition (SVD) for the matrix A let's break it down step by step.

 1. compute A.A^T:
    First, we need to calculate the matrix A.A^T(where A^T  is the transpose of matrix A):

2. find the Eingenvalues of A.A^T:
    To find the eigenvalues of A.A^T, we solve the characteristic equation:

3. Find the Right Singular Vectors (Eigenvectors of A^T.A)

4. Compute the Left Singular Vectors (Matrix U):

5.  Final SVD Equation:
    Finally, the Singular Value Decomposition of matrix A is:A=UΣV^T

## 6. Mathematical Example: Computing SVD by Hand

Consider the following matrix $A$:

$$
A = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}
$$

Our goal is to decompose $A$ into three matrices: $U$, $\Sigma$, and $V^T$, such that $A = U\Sigma V^T$.

### Step 1: Compute $A^TA$

First, calculate the transpose of $A$ and multiply it by $A$:

$$
A^TA = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 9 & 0 \\ 0 & 4 \end{bmatrix}
$$

### Step 2: Find Eigenvalues ($\lambda$)

Solve the characteristic equation $\det(A^TA - \lambda I) = 0$:

$$
\det\left(\begin{bmatrix} 9 - \lambda & 0 \\ 0 & 4 - \lambda \end{bmatrix}\right) = 0
$$

$$
(9 - \lambda)(4 - \lambda) = 0
$$

Therefore, the eigenvalues (ordered from largest to smallest) are:

$$
\lambda_1 = 9, \quad \lambda_2 = 4
$$

### Step 3: Calculate Singular Values ($\sigma$)

Singular values are the square roots of the eigenvalues ($\sigma_i = \sqrt{\lambda_i}$):

$$
\sigma_1 = \sqrt{9} = 3, \quad \sigma_2 = \sqrt{4} = 2
$$

Place these values along the main diagonal of $\Sigma$:

$$
\Sigma = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}
$$

### Step 4: Find Right Singular Vectors ($V$)

Calculate the normalized eigenvectors of $A^TA$ using $(A^TA - \lambda_i I)v_i = 0$:

* For $\lambda_1 = 9$:
  $$v_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$

* For $\lambda_2 = 4$:
  $$v_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

Combine the eigenvectors as columns to form $V$, then take its transpose $V^T$:

$$
V = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \implies V^T = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

### Step 5: Calculate Left Singular Vectors ($U$)

Compute each column of $U$ using the formula $u_i = \frac{1}{\sigma_i} A v_i$:

* For the first vector ($\sigma_1 = 3$):
  $$u_1 = \frac{1}{3} \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$

* For the second vector ($\sigma_2 = 2$):
  $$u_2 = \frac{1}{2} \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

Combine these vectors as columns to form $U$:

$$
U = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

### Step 6: Final SVD Decomposition

Putting all three matrices together gives the full decomposition $A = U\Sigma V^T$:

$$
\begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

Multiplying these three matrices reconstructs the original matrix $A$ exactly.

---

## 7. Low-Rank Approximation

SVD allows us to compress data by keeping only the $k$ largest singular values and setting the rest to zero. 

In our example, if we keep only the largest singular value ($\sigma_1 = 3$) and drop $\sigma_2$:

$$
\Sigma_1 = \begin{bmatrix} 3 & 0 \\ 0 & 0 \end{bmatrix}
$$

Reconstructing the matrix with $\Sigma_1$ yields the rank-1 approximation $A_1$:

$$
A_1 = U\Sigma_1 V^T = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 3 & 0 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 3 & 0 \\ 0 & 0 \end{bmatrix}
$$

This **Low-Rank Approximation** reduces the amount of information stored while preserving the strongest underlying component of the data.

---

## 8. Applications of SVD

* **Dimensionality Reduction:** Projecting high-dimensional data onto fewer components.
* **Data Compression:** Storing only the top singular values and vectors to save space.
* **Noise Reduction:** Discarding small singular values that typically represent random noise.
* **Recommendation Systems:** Uncovering latent user preferences and item features (e.g., collaborative filtering).
* **Feature Extraction:** Identifying key patterns in text (Latent Semantic Analysis) and images.

> **Note:** Because singular values represent the energy or strength of each component, keeping the top $k$ singular values guarantees the optimal rank-$k$ approximation with the lowest possible reconstruction error (measured by the Frobenius norm).

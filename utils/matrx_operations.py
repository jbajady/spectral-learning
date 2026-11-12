import numpy as np 
import pandas as pd


def prepare_matrix(data):
    X=np.array(data,dtype=float)


    X = X[~np.isnan(X).any(axis=1)]
    # X=np.unique(X,axis=0)

    n_row, n_col=X.shape


    means=np.sum(X,axis=0)/n_row

    variances =np.sum((X-means)**2,axis=0)/n_row

    stds=np.sqrt(variances)

    stds[stds==0]=1.0

    X_std=(X-means)/stds

    return X_std

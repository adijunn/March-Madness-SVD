import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np


sc = StandardScaler()
pca = PCA()
X_train = sc.fit_transform(X_train) 
X_train = sc.fit_transform(X_train) 
explained_variance = pca.explained_variance_ratio_ 

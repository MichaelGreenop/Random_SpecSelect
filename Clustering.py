# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:22:48 2021

@author: greenopm
"""

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd

def NumSpec(name):
    y = pd.read_csv(name,delimiter='\t')['Unnamed: 1']
    Y = len(y.unique())
    x = pd.read_csv(name,delimiter='\t')['#X']
    X = len(x.unique())
    return Y*X

def FullNum(name):
    z = pd.read_csv(name, delimiter='\t')['#Y']
    Zl = len(z)
    return Zl

# Select the wavelength range 
def waves(name):
    w = pd.read_csv(name, delimiter='\t')['#Y']
    ln = int(len(w.unique()))
    length = int(len(w)/ln)
    W = np.array(w).reshape((length,ln))[0]
    return W

def Znum(name):
    full = FullNum(name)
    XY = NumSpec(name)
    w = len(waves(name))
    Z = full/XY/w
    return Z 

def HCA_cluster(name, data, clusters):
    cluster = AgglomerativeClustering(n_clusters=clusters, affinity='euclidean', linkage='ward')  
    y_pred = cluster.fit_predict(data)
    y = pd.read_csv(name,delimiter='\t')['Unnamed: 1']
    Y = int(len(y.unique()))
    x = pd.read_csv(name,delimiter='\t')['#X']
    X = int(len(x.unique()))
    Z = int(Znum(name))
    cluster_array = np.array(y_pred).reshape((Z,Y,X))
    return cluster_array

def HCA_labels(data, clusters):
    cluster = AgglomerativeClustering(n_clusters=clusters, affinity='euclidean', linkage='ward') 
    y_pred = cluster.fit_predict(data)
    labels = pd.DataFrame(y_pred)
    return labels

def Kmeans_cluster(name, data, clusters):
    kmeans = KMeans(n_clusters=clusters, random_state=0).fit(data)
    df = np.array(kmeans.labels_)
    y = pd.read_csv(name,delimiter='\t')['Unnamed: 1']
    Y = int(len(y.unique()))
    x = pd.read_csv(name,delimiter='\t')['#X']
    X = int(len(x.unique()))
    Z = int(Znum(name))
    cluster_array = np.array(df).reshape((Z,Y,X))
    return cluster_array

def Kmeans_cluster_VRI(name, data, clusters):
    kmeans = KMeans(n_clusters=clusters, random_state=0).fit(data)
    df = np.array(kmeans.labels_)
    y = pd.read_csv(name,delimiter='\t')['Unnamed: 1']
    Y = int(len(y.unique()))
    x = pd.read_csv(name,delimiter='\t')['#X']
    X = int(len(x.unique()))
    Z = int(Znum(name))
    cluster_array = np.array(df).reshape((Z*Y,X))
    return cluster_array

def Kmeans_labels(data, clusters):
    kmeans = KMeans(n_clusters=clusters, random_state=0).fit(data)
    labels = pd.DataFrame(kmeans.labels_)
    return labels
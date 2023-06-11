

import pandas as pd 
import numpy as np



class one_variable:
    """A class for common functions (methods) with the single "name" variable"""
    def __init__(self, name):
        # Initiating the variables 
        self.name = name
        
    def raw(self):
        # Reads the raw txt file data 
        raw = pd.read_csv(self.name,delimiter='\t')
        data2 = pd.DataFrame(raw)
        return data2
    
    def FullNum(self):
        #Tells you the full number of wavenumbers
        z = self.raw()['#Y']
        Zl = len(z)
        return Zl

    def NumSpec(self):
        # Tells you the number of spectra in the dataset
        y = self.raw()['Unnamed: 1']
        Y = len(y.unique())
        x = self.raw()['#X']
        X = len(x.unique())
        return Y*X

    def waves(self):
        # Determines/provides you with the wavelength range used
        w = self.raw()['#Y']
        ln = int(len(w.unique()))
        length = int(len(w)/ln)
        W = np.array(w).reshape((length,ln))[0]
        return W

    def DataMat(self): # Was DataMat2D
        # Reshapes the data into a data matrix (rows=specra,columns=wavelengths) 
        w = self.raw()['#Y']
        data = self.raw()['Unnamed: 3']
        X = int(len(w.unique()))
        Y = int(len(w)/X)
        df = np.array(data).reshape((Y,X))
        return df

class two_variables:
    """A class for common functions (methods) with two variables (name and i)"""

    def __init__(self, name, i):
        # Initiating the variables 
        self.name = name
        self.i = i
    
    def peakSel(self):
        """Tells you the index values for the rng_txt or rng_csv functions
        if you enter the wavenumbers for the range you want"""
        data = self.waves()
        result1 = np.where(data.astype(int) == self.i)
        return result1

    def peak_txt(self):
        """Selects the range (of wavenumbers) from the data matrix
        produced with the DataMat2D function previously"""
        data = one_variable(self.name).DataMat()
        Peak = data[:,self.i:]
        Mean = pd.DataFrame(Peak).T.mean()
        return Mean

class three_variables:
    """A class for common functions (methods) with three variables (name, i, and j)"""

    def __init__(self, name, i, j):
        # Initiating the variables 
        self.name = name
        self.i = i
        self.j = j
    
    def rngSel(self):
        """Tells you the index values for the rng_txt or rng_csv functions
        if you enter the wavenumbers for the range you want"""
        data = one_variable(self.name).waves()
        result1 = np.where(data.astype(int) == self.i)
        result2 = np.where(data.astype(int) == self.j)
        return result1, result2

    def rng_txt(self):
        """Selects the range (of wavenumbers) from the data matrix
        produced with the DataMat2D function previously"""
        data = one_variable(self.name).DataMat()
        Rng = data[:,self.i:self.j]
        Mean = pd.DataFrame(Rng).T.mean()
        return Mean

class four_variables:
    """A class for common functions (methods) with three variables (name, data, i, and j)"""

    # Although you don't actually use the "name" variable
    """potentially further variables using all four will be added,
    so will keep it so as to reduce confusion - the data variable not currently
    being available in the three_variable class"""

    def __init__(self, name, data, i, j):
        # Initiating the variables 
        self.name = name
        self.data = data
        self.i = i
        self.j = j

    def rng_csv(self):
        # Same as the rng_txt function but for csv files
        data = np.array(self.data)
        Rng = data[:,self.i:self.j]
        Mean = pd.DataFrame(Rng).T.mean()
        return Mean

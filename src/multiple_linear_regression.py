import numpy as np
import pandas as pd

class MultipleLinearRegression:
    def __init__(self):
        """Initializes all required variables that are used throughout the class.
        
        Parameters:
        
        Returns:
        """
        self.optimalParams = []
    
    def train(self, x, y):
        """Trains the model using the multiple linear regression algorithm.

        Parameters:
        x - 2d array containing the variables X1, ... Xn
        y - 1D array containing the values for the dependent variables

        Returns:
        optimalParams - List containing the optimal parameters for linear regression
        """

        if x.shape[0] != y.shape[0]:
            print("Mismatch in shapes between x and y. Could not train model")
            return

        # Add intercept to X
        interceptCol = np.ones((x.shape[0], 1))
        X = np.concatenate((interceptCol, x), axis=1)

        self.optimalParams = np.linalg.inv(X.T @ X) @ X.T @ y

        return self.optimalParams
        
    
    def predict(self, data):
        """Makes a prediction of the incoming data, based on the data the model is trained on

        Parameters:
        data - 2D array based on which a prediction should be made.

        Returns:
        predictions - List containing the predictions based on the provided data and most recently trained optimal parameters.
        """

        if len(self.optimalParams) == 0:
            print("Unable to make a prediction as the model has not yet been trained.")
            return
        
        # Add intercept column to data
        interceptCol = np.ones((data.shape[0], 1))
        data = np.concatenate((interceptCol, data), axis=1)

        if data.shape[1] != len(self.optimalParams):
            print(data.shape, len(self.optimalParams))
            print("The data provided does not match the shape of the trained parameters")
            return    

        predictions = data @ self.optimalParams

        return predictions
        


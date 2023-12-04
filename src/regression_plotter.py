from matplotlib.pyplot import figure, show, subplots
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np
from scipy.optimize import curve_fit

class RegressionPlotter:
    def __init__(self, model, X, Y):
        """Handles the initialization of variables for the RegressionPlotter class
        
        Parameters:
        model - The regression model to use
        X - The variables to use as features
        Y - The target variables
        
        Returns:
        """
        self.model = model
        self.data = np.concatenate((Y.reshape(-1, 1), X), axis=1)

    def plotRegression(self, featureIndices=None, behavior="line"):
        """Plots regression based on specified behavior
        
        Parameters:
        featureIndices - List of feature indices to include. Default = None, meaning use all features
        behavior - Defines what type of plot to make. Options:
            line - plots a single regression line
            plane - Plots regression plane
            multiple - Plots multiple lines in subplots

        Returns:
        """
        numFeatures = self.data.shape[1]-1
        if featureIndices == None:
            featureIndices = list(range(1, numFeatures + 1))

        if behavior == "multiple":
            self.plotMultipleRegression(featureIndices)
        else:
            for i in featureIndices:
                if behavior == "line":
                    self.plotRegressionLine(i)
                if behavior == "plane":
                    self.plotRegressionPlane(i)

    def plotRegressionLine(self, featureIndex):
        """Plot a regression line of data considering a single feature
        
        Parameters:
        featureIndex - the index of the feature to plot from self.data
        
        Returns:
        """
        x = self.data[:, featureIndex]
        y = self.data[:, 0]

        def model(x,a,b):
            return a*x + b
        
        popt,pcov = curve_fit(model, x, y)
        perr = np.sqrt(np.diag(pcov))
        xFit = np.linspace(min(x), max(x), 1000)
        yFit = [model(x, *popt) for x in xFit]

        fig = figure()
        frame = fig.add_subplot()
        frame.scatter(x,y, label=f"Feature {featureIndex}")
        frame.plot(xFit, yFit, label="Linear fit", c="r")
        frame.set_xlabel(f"Feature {featureIndex}")
        frame.set_ylabel("Target variable")
        frame.set_title(f"Linear regression line\nY = ({popt[0]:.3f}±{perr[0]:.2f})x + ({popt[1]:.3f}±{perr[1]:.2f})")
        frame.legend()
        show()

    def plotRegressionPlane(self, featureIndex):
        """Plot a regression plane of data considering a single feature and predicting the second
        
        Parameters:
        featureIndex - the index of the feature to plot from self.data
        
        Returns:
        """
        x = self.data[:, featureIndex]
        y = self.data[:, 0]
        z = self.model.predict(self.data[:, 1:])

        fig = figure()
        frame = fig.add_subplot(111, projection="3d")
        frame.scatter(x,y,z, label=f"Feature {featureIndex}")
        frame.set_xlabel(f"Feature {featureIndex}")
        frame.set_ylabel("Target variable")
        frame.set_zlabel("Predicted target variable")
        frame.set_title("Linear regression plane")
        frame.legend()
        show()

    def calculateSubplotLayout(self, nPlots):
        """Calculates the optimal layout of rows and columns to plot in subplots
        
        Parameters:
        nPlots - the number of plots to create
        
        Returns:
        nRows - The number of rows to use
        nCols - The number of columns to use
        """

        if nPlots == 1:
            return (1,1)
        
        nCols = math.ceil(math.sqrt(nPlots))
        nRows = math.ceil(nPlots/nCols)

        return (nRows, nCols)

    def plotMultipleRegression(self, featureIndices):
        """Plots all feature indices against the target values in a 2D grid of subplots.
        
        Parameters:
        featureIndices - List of indices of data to plot from self.data
        
        Returns:
        """
        nRows, nCols = self.calculateSubplotLayout(len(featureIndices))
        fig, axs = subplots(nRows, nCols)
        for i in range(nRows):
            for j in range(i,nCols):
                x = self.data[:, i+j]
                y = self.data[:, 0]

                if nRows == 1:
                    axs[j].scatter(x,y, label=f"Feature {j+1}")
                else:
                    axs[i,j].scatter(x,y, label=f"Feature {i+j+1}")
            
        for ax in axs.flat:
            ax.legend()
            ax.label_outer()

        show()




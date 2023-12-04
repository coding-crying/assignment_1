from multiple_linear_regression import MultipleLinearRegression
from regression_plotter import RegressionPlotter
import pandas as pd
import numpy as np

def main():
    # Format data
    filename = "diabetes.txt"
    categoricals = ["SEX"]
    df = pd.read_csv(filename, sep="\t")

    for cat in categoricals:
        df = df.drop(cat, axis=1)   # Remove all columns containing categorical variables

    Y = df["Y"].to_numpy()
    df = df.drop("Y", axis=1)
    X = df.to_numpy()

    # Create model
    MLR = MultipleLinearRegression()
    MLR.train(X, Y)

    RP = RegressionPlotter(MLR, X, Y)
    RP.plotRegression(featureIndices=[1,2,3], behavior="multiple")

main()
    


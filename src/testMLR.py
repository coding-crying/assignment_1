from multiple_linear_regression import MultipleLinearRegression
import pandas as pd
from matplotlib.pyplot import figure,show
from sklearn.linear_model import LinearRegression
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

    predictData = X[:20]
    # Own model prediction
    MLR = MultipleLinearRegression()
    MLR.train(X, Y)
    prediction = MLR.predict(predictData)
    
    # Package prediction
    reg = LinearRegression()
    reg.fit(X,Y)
    skcoeff = np.concatenate(([reg.intercept_], reg.coef_))
    skpred = reg.predict(predictData)

    # Comparison
    print(f"Own coefficients: {MLR.optimalParams}\nsklearn coefficients: {skcoeff}")
    print(f"Own predictions: {prediction}\nsklearn predictions: {skpred}")
    
    xPlot = list(range(len(prediction)))
    fig = figure()
    frame = fig.add_subplot()
    frame.scatter(xPlot, Y[:20], label="Actual data")
    frame.scatter(xPlot, prediction, label="Own model")
    frame.scatter(xPlot, skpred, label="sklearn prediction")
    frame.set_title("Predictions of own MLR model vs sklearn model")
    frame.set_xlabel("Data index")
    frame.set_ylabel("Y values")
    frame.legend()
    show()

main()
    
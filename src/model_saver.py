import numpy as np
import pandas as pd

class ModelSaver:
    def __init__(self, format, filename):
        """Sets the attributes for the ModelSaver class

        Parameters:
        format - The file format to import/export to
        filename - The filename to import/export to

        Returns:
        """
        self.format = format
        self.filename = filename

    def getAndSave(self, model):
        """Gets and saves the parameters from a given model
        
        Parameters:
        model - The model to get the optimal parameters from
        
        Returns:
        """

        params = model.getParams()
        df = pd.DataFrame(params)
        
        if self.format == "csv":
            df.to_csv(self.filename)
            return
        elif self.format == "json":
            df.to_json(self.filename)
            return
        elif self.format == "pickle":
            df.to_pickle(self.filename)
            return
        else:
            print(f"Unhandled export format: {self.format}")

    
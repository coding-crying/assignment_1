# OOP - 2023/24 - Assignment 1

This is the base repository for assignment 1.
Please follow the instructions given in the [PDF](https://brightspace.rug.nl/content/enforced/243046-WBAI045-05.2023-2024.1/2023_24_OOP.pdf) for the content of the exercise.

## How to carry out your assignment

Fork this repo on your private github account.
You can do so by clicking this button on the top-right panel:
![](fork.png) 

The assignment is divided into 4 blocks.
Block 1, 2, and 3 all define different classes.

Put the three classes in three separate files in the `src` folder, with the names specified in the PDF.
**Leave the __init__.py file untouched**.

Put the **main.py** script **outside** of the `src` folder, in the root of this repo.

Below this line, you can write your report to motivate your design choices.

## Submission

The code should be submitted on GitHub by opening a Pull Request from the branch you were working on to the `submission` branch.

There are automated checks that verify that your submission is correct:

1. Deadline - checks that the last commit in a PR was made before the deadline
2. Reproducibility - downloads libraries included in `requirements.txt` and runs `python3 src/main.py`. If your code does not throw any errors, it will be marked as reproducible.
3. Style - runs `flake8` on your code to ensure adherence to style guides.

---

## Your report

## Multiple Liner Regression

### Public Variable

1. **`coefficients` (Public Variable)**:
    - **Role**: Stores the coefficients of the regression model after training.
    - **Reason for Being Public**:
        - **Direct Access**: Allows users of the class to directly access the model's coefficients after training, which is a common requirement in linear regression analysis.
        - **Transparency**: Provides transparency about the model's state, enabling users to understand and interpret the model.

### Private Variables and Methods


1. **Internal Variables and Operations in Methods (`train`, `predict`, `get_coefficients`)**:
    - **Role**: Variables and operations within these methods handle the internal logic of training, prediction, and coefficient retrieval.
    - **Reason for Being Private**:
        - **Implementation Details**: The internal workings of the methods (like matrix operations in `train` and `predict`) are specific to the implementation and are not meant to be accessed or modified directly from outside the class.
        - **Data Integrity**: Keeping these details encapsulated ensures the integrity of the model’s training and prediction processes.

### Design Considerations

- **Encapsulation**: By keeping certain variables and operations internal to the methods, the class encapsulates its behavior, exposing only what is necessary (like the `coefficients`) to the outside world.
    
- **User-Friendly Interface**: The public methods (`train`, `predict`, `get_coefficients`) provide a clear and user-friendly interface for interacting with the class, abstracting away the complex operations involved in regression analysis.
    
- **Maintainability and Extensibility**: This approach ensures that the internal implementation can be modified without affecting the external interface of the class, making it easier to maintain and extend.
## Regression_plotter:

#### Public Variables and Methods

1. **`model` (Public Variable)**:
    
    - **Purpose**: Holds the regression model instance.
    - **Why Public**: The model is a fundamental part of the `RegressionPlotter` and is intended to be set at initialization and potentially accessed or modified later. Making it public allows for direct access and manipulation outside the class if necessary (for example, to update the model or retrieve its parameters).
2. **`plot` (Public Method)**:
    
    - **Purpose**: The main interface for users to plot regression lines or planes.
    - **Why Public**: This is the primary functionality of the class. It is designed to be called externally with the required data (`X` and `y`). It intelligently delegates to the appropriate private method based on the number of features.

#### Private Methods

1. **`_plot_line`, `_plot_plane`, `_plot_multiple` (Private Methods)**:
    - **Purpose**: Handle the specifics of plotting for different scenarios (one feature, two features, multiple features).
        
    - **Why Private**: These methods are specific internal implementations of the plotting logic. They are not intended to be called directly from outside the class. Marking them as private (with the leading underscore) indicates that they are implementation details, and users of the class should not rely on them directly. This encapsulation also allows for future changes to the internal plotting logic without affecting external users of the class.

#### Design Decisions
- **Encapsulation**: The internal workings of the class (the specific plotting methods) are hidden from the user. This encapsulation protects the internal state and behavior of the class and allows for easier maintenance and potential future enhancements.
    
- **Abstraction**: The `plot` method provides a high-level abstraction over the different plotting scenarios. Users of the class interact with this simple interface, while the complex logic is abstracted away in private methods.
## Model Saver
### Public Methods

1. **Initialization (`__init__`)**:
    
    - Initializes the class with a specified format (`csv` or `json`).
    - Validates the format to ensure it's either 'csv' or 'json'.
2. **Saving Parameters (`save_parameters`)**:
    
    - Saves the model's parameters to a file in the chosen format.
    - Handles both CSV and JSON formats, converting NumPy arrays to lists for JSON.
3. **Loading Parameters (`load_parameters`)**:
    
    - Loads parameters from a file and sets them in the given model.
    - Reads from CSV or JSON files and converts the data to NumPy arrays before setting them in the model.
4. **Setting Format (`set_format`)**:
    
    - Allows changing the format for saving and loading parameters.

### Private Variable

1. **`_format` (Private Variable)**:
    - Stores the chosen format for saving and loading parameters.
    - **Reason for Being Private**:
        - Encapsulation: Keeps the format internal to the class, preventing external modification without validation.
        - Controlled Access: Changes to the format are done through the `set_format` method, ensuring validation.

### Design Considerations

- **Flexibility in Format Handling**: Supports multiple formats (CSV and JSON) for saving and loading, providing flexibility depending on use cases.
    
- **Validation of Format**: Ensures that only supported formats are used, adding robustness to the class.
    
- **Ease of Integration**: Can work with any model that has `get_parameters` and `set_parameters` methods, making it versatile.
    
- **Handling NumPy Arrays**: Converts NumPy arrays to lists when saving in JSON format, considering JSON’s limitations with NumPy array serialization.
    
- **Abstraction and Convenience**: Abstracts away the file handling and format-specific operations, providing a simple interface for saving and loading model parameters.
    

### Technical Considerations

- **Dependency on NumPy and Standard Libraries**: Utilizes NumPy for array handling and standard libraries `csv` and `json` for file operations.
    
- **Generic Model Compatibility**: Designed to be agnostic to the model type, as long as the model conforms to the expected interface (`get_parameters` and `set_parameters`).

For the dataset diabetes.txt, this is the attribute information:
age age in years
sex
bmi body mass index
bp average blood pressure
s1 tc, total serum cholesterol
s2 ldl, low-density lipoproteins
s3 hdl, high-density lipoproteins
s4 tch, total cholesterol / HDL
s5 ltg, possibly log of serum triglycerides level
s6 glu, blood sugar level

Because sex is a categorical variable, we will remove it for comparison with an MLR from a package. This is applied in testMLR.py, the output of which is:
Own coefficients: [-3.63898716e+02 -1.20515114e-01  6.00406612e+00  9.50507937e-01
 -9.80784274e-01  6.58496188e-01  5.13628212e-01  4.65988116e+00
  6.89473421e+01  2.02625303e-01]
sklearn coefficients: [-3.63898716e+02 -1.20515114e-01  6.00406612e+00  9.50507937e-01
 -9.80784274e-01  6.58496188e-01  5.13628212e-01  4.65988116e+00
  6.89473421e+01  2.02625303e-01]
Own predictions: [215.96752121  63.41589184 186.67691925 156.33694689 115.81197916
 103.25635897  86.75971231 127.06347839 171.51374095 208.28740647
  85.63412266 100.21574365 107.9324862  177.25210152  98.78680101
 180.99101205 208.26900779 187.91555483 136.95837839 120.04595369]
sklearn predictions: [215.96752121  63.41589184 186.67691925 156.33694689 115.81197916
 103.25635897  86.75971231 127.06347839 171.51374095 208.28740647
  85.63412266 100.21574365 107.9324862  177.25210152  98.78680101
 180.99101205 208.26900779 187.91555483 136.95837839 120.04595369]

 As you can see, the package creates the exact same results.

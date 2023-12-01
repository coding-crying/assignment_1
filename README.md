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

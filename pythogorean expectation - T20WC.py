import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
import csv

data = pd.read_csv('T20WC Matches.csv')

data['WinRatio'] = data['MatchesWon']/data['MatchesPlayed']
data['PythogoreanExpectation'] = data['Runs']**2/(data['Runs']**2 + data['OppRuns']**2)

sns.regplot(x = 'PythogoreanExpectation', y = 'WinRatio', data = data)
plt.xlabel('Pythogorean Expectation')
plt.ylabel('Win Ratio')
plt.title("Relationship between win ratio and pythogorean expectation")

regression = smf.ols(formula = 'WinRatio ~ PythogoreanExpectation', data = data).fit()
print(regression.summary())
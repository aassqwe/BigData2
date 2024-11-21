import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

mpg = sns.load_dataset('mpg')
mpg.drop(['name'], axis=1, inplace=True)
mpg.dropna(inplace=True)
mpg = pd.get_dummies(mpg, columns=['origin'], drop_first=True)
# print(mpg.info())

X = mpg.drop(['mpg'], axis=1)
y = mpg['mpg']

print(y)
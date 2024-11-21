import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

mpg = sns.load_dataset('mpg')
print(mpg.info())
mpg.dropna(inplace=True)
print(mpg.info())
print(mpg.head())
print(mpg.tail())
print(mpg[['origin']])
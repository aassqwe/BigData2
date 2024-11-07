import seaborn as sns
import pandas as pd
import matplotlib.pylab as plt


titanic = sns.load_dataset('titanic')
# print(titanic['sex'].head())
# print(titanic.info())
# gender_survival = titanic.groupby(by='sex')['survived'].mean()
# print(gender_survival)
gender_survival = titanic.groupby(by='sex')['survived'].mean().reset_index()
print(type(gender_survival))
print(titanic.info())
sns.barplot(data=gender_survival, x='sex', y='survived')
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.show()


# titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
# titanic['deck'].fillna('Unknown', inplace=True)
# print(titanic['deck'])
# print(titanic.info())
# print(titanic['survived'])
# print(titanic.info())
# sns.countplot(data=titanic, x='survived')
# plt.title('Survived (0 = No, 1 = Yes)')
# plt.xlabel('Survived')
# plt.ylabel('Count')
# plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split


# 나이에 따른 생존율 계산
titanic = sns.load_dataset('titanic')
median_age = titanic['age'].median()
titanic_fill_row = titanic.fillna({'age' : median_age})

X = titanic_fill_row[['age']]
y = titanic_fill_row['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = KNeighborsRegressor(n_neighbors=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)
print(y_test)

plt.figure(figsize=(5, 2))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.title('Linear Regression: Real vs predicted')
plt.xlabel('Age')
plt.ylabel('Survivied')
plt.show()


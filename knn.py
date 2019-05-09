import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = pd.read_csv('Top100.csv')

X = data
X = X.drop(['id', 'name', 'artists', 'time_signature'], axis=1)
y = data['id']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

scores = []
ks = []
best_score = 0.0

for k in range(1, 25):
    knclf = KNeighborsClassifier(n_neighbors=k)
    knclf.fit(X_train, y_train.ravel())
    y_pred = knclf.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    print("k {} score {}".format(k, score))
    scores.append(score)
    ks.append(k)
    if best_score < score:
        best_k = k
        best_score = score

print("best K value {} with a accuracy score of {}".format(best_k, best_score))

plt.plot(scores)
plt.ylabel('Accuracy Score')
plt.xlabel('K Neighbors')
plt.show()

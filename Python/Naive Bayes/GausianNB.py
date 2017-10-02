import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[-1, -1], [-2, 1], [0, 1], [3, 2], [-3, -2]])
Y = np.array([1, 1, 2, 2, 2])

clf = GaussianNB()
clf.fit(X, Y)
pred = clf.predict([[-0.8, -1]])
print (pred)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(pred, Y)

print accuracy


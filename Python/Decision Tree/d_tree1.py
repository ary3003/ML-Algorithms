#!/usr/bin/python

# This is the main script for the algorithm

# Sara has label 0
# chris has label 1

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


from sklearn import tree

clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
print accuracy_score(pred, labels_test)

print len(features_train[0])

# This is the main script for the algorithm

from class_vis import prettyPicture
from sklearn.tree import DecisionTreeClassifier
from prep_terrain_data import makeTerrainData
from sklearn.ensemble import AdaBoostClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()

# you can change the min_samples_split and then check the test.png file to know the difference
dt = DecisionTreeClassifier(min_samples_split=50)
clf = AdaBoostClassifier(n_estimators=100,base_estimator=dt,learning_rate=1)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

# should be 92.8%
print "Decision tree accuracy after using AdaBoost is: ",acc

prettyPicture(clf, features_test, labels_test)

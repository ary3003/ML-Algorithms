from class_vis import prettyPicture
from sklearn.tree import DecisionTreeClassifier
from prep_terrain_data import makeTerrainData

# This is the main script for the algorithm to test using the self driving example
# you remember it. Just try to think wisely if you are coming back after long time.

features_train, labels_train, features_test, labels_test = makeTerrainData()

# you can change the min_samples_split and then check the test.png file to know the difference
clf = DecisionTreeClassifier(min_samples_split=50)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

# should be 90.8%
print "Decision tree accuracy is: ",acc

prettyPicture(clf, features_test, labels_test)

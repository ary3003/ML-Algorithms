from class_vis import prettyPicture

from prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData()

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=10)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

# should be 92.8 as checked for n_estimators = 10.
print "Random Forest accuracy is: ",acc

prettyPicture(clf, features_test, labels_test)

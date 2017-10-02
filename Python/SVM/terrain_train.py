from prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData()

from sklearn.svm import SVC

clf = SVC(kernel="linear")

clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

#should be 92%
print "SVM accuracy is: ", acc

from class_vis import prettyPicture

prettyPicture(clf, features_test, labels_test)
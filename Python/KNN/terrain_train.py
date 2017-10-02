from class_vis import prettyPicture
from sklearn.neighbors import KNeighborsClassifier
from prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData()

# more the number of neighbours less will be the accuracy.
clf = KNeighborsClassifier(n_neighbors=1)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

# should be 94% as checked for n_neighbours = 1.
print "K Nearest Neighbours accuracy is: ",acc

prettyPicture(clf, features_test, labels_test)

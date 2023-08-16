from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecesionTreeClassifier()
clf = clf.fit(features, labels)
print clg.predit([[150, 0]])

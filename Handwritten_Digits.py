from sklearn import tree
data = [[150,1],[130,0],[170,1],[140,0]]
labels = [1,0,1,0]
Classifier=tree.DecisionTreeClassifier()
Classifier.fit(data,labels)
print(Classifier.predict([[100,0]]))
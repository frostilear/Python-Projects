from scipy.spatial import distance
def euc(a,b):
    return distance.euclidean(a, b)
    

class ScrappyKNN():
    def fit(self, X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
        
        
    
    def predict(self, X_test):
        predections = []
        for row in X_test:
            
            label =  self.closest(row)
            predections.append(label)
        return predections
        
    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        
        for i in range(1, len(self.X_train)):
            
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.Y_train[best_index]
                    
          
from sklearn.datasets import load_iris
iris = load_iris()

X= iris.data
Y= iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = .5)


my_class = ScrappyKNN()
my_class .fit(X_train, Y_train)
prediction = my_class.predict(X_test)
print (prediction)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, prediction))
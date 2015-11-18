# Setosa, Versicolour, and Virginica
# Sepal Length, Sepal Width, Petal Length and Petal Width.

import sklearn
from sklearn import datasets
from sklearn import svm
import numpy as np
from sklearn import cross_validation
from sklearn.metrics import accuracy_score,accuracy_score, confusion_matrix

iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)


model = svm.SVC()
model.fit(X_train,y_train)

#pred =  model.predict([[2,2,2,2]])
pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print 'Prediction:'
print pred

print ''

print 'Accuracy of: ', accuracy
print ''
print 'Confusion Matrix:'
print confusion_matrix(y_test, pred)

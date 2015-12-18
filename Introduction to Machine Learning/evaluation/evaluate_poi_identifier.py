#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation
import numpy as np
from sklearn.metrics import *


data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here

features_train,features_test,labels_train,labels_test = cross_validation.train_test_split(features,labels,test_size=0.3,
                                                                                          random_state=42)
clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)
clf.score(features_test,labels_test)
clf.predict(features_test)

precision_score(labels_test,clf.predict(features_test))

recall_score(labels_test,clf.predict(features_test))

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

precision_score(true_labels,predictions)
recall_score(true_labels,predictions)

print precision_score(true_labels,predictions)

print recall_score(true_labels,predictions)

print clf.score(features_test,labels_test)

print clf.predict(features_test)

print np.array(labels_test)

print (1.0 - 5.0/29)

print len([e for e in labels_test if e == 1.0])

print len(labels_test)

print precision_score(labels_test,clf.predict(features_test))

print recall_score(labels_test,clf.predict(features_test))

print precision_score(true_labels,predictions)

print recall_score(true_labels,predictions)



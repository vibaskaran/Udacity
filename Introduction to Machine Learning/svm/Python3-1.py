#!/usr/bin/env python3

import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from sklearn import tree
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################



#### your code goes here

clf = tree.DecisionTreeClassifier() 
clf = clf.fit(features_train, labels_train)
prediction = clf.predict(features_test)
#print accuracy_score(prediction, labels_test)

acc = accuracy_score(prediction, labels_test)
### be sure to compute the accuracy on the test set


    
def submitAccuracies():
  return {"acc":round(acc,3)}

{"message": "{'acc_min_samples_split_50': 0.912, 'acc_min_samples_split_2': 0.908}"}


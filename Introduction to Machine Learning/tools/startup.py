#!/usr/bin/python
print
print "unzipping Enron dataset (this may take a while)"
import tarfile
import os
os.chdir("..")
#tfile = tarfile.open("c:\Users\Viswanathanb\Documents\GitHub\Udacity\Introduction to Machine Learning\enron_mail_20150507.tgz", "r:gz")
tfile = tarfile.open("enron_mail_20150507.tgz", "r:gz")
tfile.extractall(".")

print "you're ready to go!"

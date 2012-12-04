"""
http://orange.biolab.si/doc/ofb/c_basics.htm
http://orange.biolab.si/doc/ofb/c_performance.htm

"""
import Orange,numpy, os, orange
from Orange.regression import earth
from matplotlib import pylab as pl
from numpy import *
import matplotlib.pyplot as plt

# Change working directory to get data
#os.chdir("C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507--Project-3")
#os.chdir('C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507HW/MCS 507 Homework 4/MCS507--Project-3')
#os.chdir('C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507_Final_Project')


data = orange.ExampleTable("adult")
print data.domain.attributes
print data[:4]

data_test=data


########################
# Build Classifier
########################

import orange, orngTest, orngStat, orngTree   
classifier = orange.BayesLearner(data)
bayes = orange.BayesLearner()
bayes.name = "bayes"
learners = [bayes]

results = orngTest.crossValidation(learners, data, folds=10)

# output the results
print "Learner CA IS Brier AUC"
for i in range(len(learners)):
    print "%-8s %5.3f %5.3f %5.3f %5.3f" % (learners[i].name, \
    orngStat.CA(results)[i], orngStat.IS(results)[i], orngStat.BrierScore(results)[i], orngStat.AUC(results)[i])

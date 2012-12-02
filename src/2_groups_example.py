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
os.chdir('C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507_Final_Project')


########################
# Functions to split the data
########################


def unique(data, class_col):
    """
    Creates a list of unique obversations from data
    class_col=the column number containing the group
    """
    groups=[]
    for i in range(len(data)):
        # Check to see if this group has been added to groups
        if data[i][class_col] not in groups:
            groups.append(data[i][class_col])
    return groups


# Split the data into unique groups
def unique_split(data,class_col):
    # Get the list of unique groups
    r=unique(data,class_col)
    p=[]
    for q in range(len(r)):
        p.append([])
    for i in range(len(data)):
        #print i
        for j in range(len(r)):
            #print j
            if data[i][class_col]==r[j]:
                p[j].append(data[i])

    return p


data = orange.ExampleTable("2_groups")
print data.domain.attributes
print data[:4]

# Get a small amount of data
index=Orange.data.sample.SubsetIndices2(p0=0.10)
ind=index(data)
#data_test=data.select(ind,0)
data_test=data


########################
# Split the data
########################

X, Y = data_test.to_numpy("A/C")
data_2=[]
for i in range(len(Y)):
    data_2.append([X[i][0],X[i][1],Y[i]])
p=unique_split(data_2,2)

# Group 1
X11=[p[0][i][0] for i in range(len(p[0]))]
X12=[p[0][i][1] for i in range(len(p[0]))]

# Group 2
X21=[p[1][i][0] for i in range(len(p[1]))]
X22=[p[1][i][1] for i in range(len(p[1]))]

### Group 3
##X31=[p[2][i][0] for i in range(len(p[2]))]
##X32=[p[2][i][1] for i in range(len(p[2]))]

# Obtain the counts
##len(X11);len(X21);len(X31)
len(X11);len(X21);

########################
# Plot the data
########################


import matplotlib.pyplot as plt
import matplotlib
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(X11, X12, s=10, c='b', marker="+")
ax1.scatter(X21, X22, s=10, c='c', marker="o")
#ax1.scatter(X31, X32, s=10, c='y', marker="x")
plt.title('Plot of Three Classes of Data')
plt.show()

########################
# Build Classifier
########################

import orange, orngTest, orngStat, orngTree   
classifier = orange.BayesLearner(data)
bayes = orange.BayesLearner()
bayes.name = "bayes"
learners = [bayes]

results = orngTest.crossValidation(learners, data_test, folds=10)

########################
# Compute the misclassified observations
########################

X, Y = data_test.to_numpy("A/C")
data_scored=[]
for i in range(len(results.results)):
    if results.results[i].classes[0]==results.results[i].actual_class:
        data_scored.append(1)
    else:
        data_scored.append(0)

import matplotlib.pyplot as plt
import matplotlib

X1w=[];X2w=[]
for i in range(len(X)):
    if data_scored[i]==0:
        X1w.append(X[i][0])
        X2w.append(X[i][1])



########################
# Plot the misclassified data
########################
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(X11, X12, s=10, c='b', marker="+")
ax1.scatter(X21, X22, s=10, c='c', marker="o")
#ax1.scatter(X31, X32, s=10, c='y', marker="x")
ax1.scatter(X1w, X2w, s=10, c='m', marker="^")
plt.title('Plot of Three Classes of Data, Showing the Misclassified Elements')
plt.show()
    
# output the results
print "Learner CA IS Brier AUC"
for i in range(len(learners)):
    print "%-8s %5.3f %5.3f %5.3f %5.3f" % (learners[i].name, \
    orngStat.CA(results)[i], orngStat.IS(results)[i], orngStat.BrierScore(results)[i], orngStat.AUC(results)[i])
            

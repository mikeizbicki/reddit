#!/usr/bin/env python

import csv
import sys
import numpy as np
import scipy.io
from sklearn import mixture
from sklearn import linear_model
from sklearn.cross_validation import KFold,StratifiedKFold
from sklearn.linear_model import LassoCV
from sklearn.externals import joblib

################################################################################
# load data

filename_csv = sys.argv[1]
startdp_ratio = float(sys.argv[2])/100
stopdp_ratio = float(sys.argv[3])/100

# load csv file

print "loading csv file"
inputfile=open(filename_csv)
input=csv.DictReader(inputfile)

print "creating Y"
Y=map(lambda x: x["score"],list(input))
startdp=int(len(Y)*startdp_ratio)
stopdp=int(len(Y)*stopdp_ratio)
Ymod=Y[startdp:stopdp]

# load matrix

print "loading matrix"
X=scipy.io.loadmat(filename_csv+".mat")["counts"]
Xmod=X[startdp:stopdp,:]

################################################################################
# compute model

print "training model"

model = LassoCV(n_jobs=-1,n_alphas=8,verbose=10)
model.fit(Xmod,Ymod)

print model.coef_
print model.mse_path_

joblib.dump(model,filename_csv+".model-"+str(startdp_ratio)+"-"+str(stopdp_ratio))


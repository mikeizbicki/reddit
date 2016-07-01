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

print ("filename: "+filename_csv+"; startdp_ratio="+str(startdp_ratio)+"; stopdp_ratio="+str(stopdp_ratio))
sys.stdout.flush()

# load csv file

print "loading csv file"
sys.stdout.flush()
inputfile=open(filename_csv)
input=csv.DictReader(inputfile)

print "creating Y"
sys.stdout.flush()
Y=map(lambda x: x["score"],list(input))
startdp=int(len(Y)*startdp_ratio)
stopdp=int(len(Y)*stopdp_ratio)
Ymod=Y[startdp:stopdp]

#for y in Ymod:
    #print y

# load matrix

print "loading matrix"
sys.stdout.flush()
X=scipy.io.loadmat(filename_csv+".mat")["counts"]
Xmod=X[startdp:stopdp,:]

################################################################################
# compute model

print "training model"
sys.stdout.flush()

model = LassoCV(n_jobs=-1,n_alphas=8,verbose=10)
model.fit(Xmod,Ymod)

print "done. model specs:"
sys.stdout.flush()
print model.coef_
print model.mse_path_

print "saving model"
sys.stdout.flush()
joblib.dump(model,filename_csv+".model-"+str(startdp_ratio)+"-"+str(stopdp_ratio))


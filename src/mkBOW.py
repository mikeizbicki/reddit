#!/usr/bin/env python

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import scipy.io
import csv
import sys

# load csv file

print "loading vocabulary"
vocab=open("words").read().splitlines()

print "loading csv file"
inputfile=open(sys.argv[1])
input=csv.DictReader(inputfile)

# get ngram counts

print "vectorizing"
vectorizer = CountVectorizer(
    vocabulary=vocab,
    ngram_range=(1,1)
    #token_pattern=r'\b\w_\b',
    #binary=True,
    #min_df=1
    #strip_accents='unicode',
    )
counts = vectorizer.fit_transform(
    map(lambda a: a["body"], list(input))
    )

# create tfidf counts

#print "calculating tfidf"
#transformer=TfidfTransformer()
#counts = transformer.fit_transform(counts)

# generate output

print "saving matrix"
scipy.io.savemat(sys.argv[1]+".mat", {"counts":counts})

#print counts.shape
#print counts

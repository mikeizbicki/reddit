#!/usr/bin/env python

import csv
import json
import sys
from collections import OrderedDict

inputFile = open(sys.argv[1])
outputFile = open(sys.argv[1]+".csv","w")
output = csv.writer(outputFile)
#output = csv.writer(sys.stdout)

i=0
oldkeys="start"
for line in inputFile:
    if i%100==0:
        print "iteration: ", i
    i+=1

    data = OrderedDict(sorted(json.loads(line).items()))

    def tostr(x):
        if type(x) is type(u""):
            return x.encode("utf-8").encode('string_escape')
            #return x.encode("utf-8")
        elif type(x) is int:
            return str(x)
        else:
            return str(x) #"None"

    if oldkeys == "start":
        output.writerow(map(tostr,data.keys()))
    else:
        if not (oldkeys == data.keys()):
            print "iteration: ", i
            print "  error: oldkeys != data.keys()"
            print "oldkeys    =", oldkeys
            print "data.keys()=", data.keys()
    oldkeys=data.keys()

    output.writerow(map(tostr,data.values()))


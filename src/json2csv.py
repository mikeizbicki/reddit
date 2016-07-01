#!/usr/bin/env python

import csv
import json
import sys
from collections import OrderedDict

inputFile = open(sys.argv[1])
outputFile = open(sys.argv[1]+".csv","w")
output = csv.writer(outputFile)
#output = csv.writer(sys.stdout)

header=[u'archived', u'author', u'author_flair_css_class', u'author_flair_text', u'body', u'controversiality', u'created_utc', u'distinguished', u'downs', u'edited', u'gilded', u'id', u'link_id', u'name', u'parent_id', u'removal_reason', u'retrieved_on', u'score', u'score_hidden', u'subreddit', u'subreddit_id', u'ups']

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

    for key in header:
        if not key in data:
            data[key]='XXX'
            data=OrderedDict(sorted(data.items()))

    if oldkeys == "start":
        output.writerow(header)
    else:
        if not (oldkeys.sort() == data.keys().sort()):
            print "iteration: ", i
            print "  error: oldkeys != data.keys()"
            print "oldkeys    =", oldkeys
            print "data.keys()=", data.keys()
            quit()
    oldkeys=data.keys()

    output.writerow(map(tostr,data.values()))


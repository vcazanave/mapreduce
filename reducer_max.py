#!/usr/bin/python
import sys
costMax = 0.0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisCost = data
	thisCost = float(thisCost)
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey,costMax)
		costMax = 0.0
	oldKey = thisKey
	costMax = max(costMax,thisCost)
if oldKey != None:
	print oldKey,"\t",costMax

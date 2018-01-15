#!/usr/bin/python
import sys
salesTotal = 0.0
nb = 0.0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisSale = data
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey,salesTotal/nb)
		salesTotal = 0.0
		nb = 0.0
	oldKey = thisKey
	salesTotal += float(thisSale)
	nb += 1.0
if oldKey != None:
	print oldKey,"\t",salesTotal/nb

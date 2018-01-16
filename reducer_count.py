#!/usr/bin/python
import sys
n = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, item = data
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey,n)
		n = 0
	oldKey = thisKey
	n += 1
if oldKey != None:
	print oldKey,"\t",n

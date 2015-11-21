#!/usr/bin/env python
import sys, argparse, csv
import numpy as np

#269 columns
# No = 0, Yes = 1, Everything else = -1

with open('trainingData.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	row1 = spamreader[0]
	for header in row1:
		if header 
			


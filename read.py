#!/usr/bin/env python
import sys, argparse, csv
import numpy as np


#269 columns
# No = -1, Yes = 1, Complete_remission = 1, resilience = 0, Everything else = -1
# NA=0
#NEG=-1, POS=1
# F = 1, M=-1
# Chemos: ANTHRA_HDAC = 0, HDAC-PLUS=1, FLU_HDAC = 2; STDARAC-PLUS = 3
REMISSED_PATIENTS = {}
RESISTANT_PATIENTS = {}
with open('trainingData.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	
	for row in spamreader:
		for ind, var in enumerate(row[1:]):
			if var == 'COMPLETE_REMISSION':
				REMISSED_PATIENTS["Patient"+str(counter)]=row
			else:
				RESISTANT_PATIENTS["Patient"+str(counter)]=row
		counter = counter+1

for patient in REMISSED_PATIENTS:
	for ind, var in enumerate(REMISSED_PATIENTS[patient]):
		# Yes/No responses
				if var in ('YES', 'COMPLETE_REMISSION', 'POS', 'F'):
					var = '1'
					REMISSED_PATIENTS[patient][ind] = var 
				if var in ('No', 'RESISTANT', 'NEG', 'M') :
					var='-1'
					REMISSED_PATIENTS[patient][ind] = var 
				# No information
				if var == 'NA':
					var = '0'
					REMISSED_PATIENTS[patient][ind] = var  

				# Chemo type
				if var == 'Anthra-HDAC':
					var = '0'
					REMISSED_PATIENTS[patient][ind] = var  
				if var == 'HDAC-Plus':
					var = '1'
					REMISSED_PATIENTS[patient][ind] = var 
				if var == 'Flu-HDAC':
					var = '2'
					REMISSED_PATIENTS[patient][ind] = var 
				if var == 'StdAraC-Plus':
					var = '3'
					REMISSED_PATIENTS[patient][ind] = var 

for patient in RESISTANT_PATIENTS:
	for ind, var in enumerate(RESISTANT_PATIENTS[patient]):
		# Yes/No responses
				if var in ('YES', 'COMPLETE_REMISSION', 'POS', 'F'):
					var = '1'
					RESISTANT_PATIENTS[patient][ind] = var 
				if var in ('No', 'RESISTANT', 'NEG', 'M') :
					var='-1'
					RESISTANT_PATIENTS[patient][ind] = var 
				# No information
				if var == 'NA':
					var = '0'
					RESISTANT_PATIENTS[patient][ind] = var  

				# Chemo type
				if var == 'Anthra-HDAC':
					var = '0'
					RESISTANT_PATIENTS[patient][ind] = var  
				if var == 'HDAC-Plus':
					var = '1'
					RESISTANT_PATIENTS[patient][ind] = var 
				if var == 'Flu-HDAC':
					var = '2'
					RESISTANT_PATIENTS[patient][ind] = var 
				if var == 'StdAraC-Plus':
					var = '3'
					RESISTANT_PATIENTS[patient][ind] = var 

print REMISSED_PATIENTS["Patient166"]
print "________________________________________________________-"
print RESISTANT_PATIENTS["Patient165"]	
			


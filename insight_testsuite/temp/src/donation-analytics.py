import sys
import numpy as np
from validate import malformed

# reading the required files and creating an empty output file
inputfile = open(sys.argv[1], 'r')
percentileValue = int(open(sys.argv[2], 'r' ).read())
file = open(sys.argv[3],'w+', newline='\n')

seen = set()    # contains donors that have contributed atleast once before
records = {}    # mapping list of contributions to (recipientID, donorZipCode, year) 

for line in inputfile:
	
	# testing if the transaction line needs to be skipped	
	if malformed(line):
		continue
	
	fields = line.split("|")

	# required fields from every transactions
	donorName = fields[7]
	donorZipCode = fields[10][:5]
	recipientID = fields[0]
	contribution = round(float(fields[14]))
	year = fields[13][-4:]

	# checking if donor is a repeat donor, & then
	# emitting the contribution of that recipient, from repeatDonors zipCode for current year
	if (donorName, donorZipCode) not in seen:
		seen.add((donorName, donorZipCode))
	else:
		transactionKey = (recipientID, donorZipCode, year)

		if transactionKey not in records:
			records[transactionKey] = []

		records[transactionKey].append(contribution)

		percentile = np.percentile(records[transactionKey], percentileValue, interpolation='lower')
		totalContributions = np.sum(records[transactionKey])
		totalTransactions = len(records[transactionKey])

		file.write("|".join(map(str,[recipientID, donorZipCode, year, percentile, totalContributions, totalTransactions]))+'\n')

file.close()
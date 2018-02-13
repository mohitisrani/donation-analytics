## All the functions to validate a tuple are included in this python file.

import re
import datetime

# to validate Date
def validateDate(date_text):
	try:
		datetime.datetime.strptime(date_text, '%M%D%Y')
		return True
	except: 
		return False



# to check if any of the required entity is malformed in the record
# or if the donation is from an organization
def malformed(record):
	l = record.split('|')
	return(l[-6] != ""                                 #not an individual entity 
		or validateDate(l[13])                         #date field empty or ill formed
		or bool(re.match("^[0-9]{0,4}$",l[10]))        #zipCode empty or less than 5 digits
		or l[7] == ""                                  #name field empty
		or bool(re.search(r'\d', l[7]))                #name field contains any number
		or not bool(re.match("^[0-9a-zA-Z]{9}$",l[0])) #CmteID empty or not a 9 digit alphanumeric code
		or l[-7] == ""                                 #TransactionAmount field empty
		)
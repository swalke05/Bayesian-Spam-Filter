#SpamFilter.py
#Spencer Walker
#0715530


#This file contains the main method for the SpamFilter. The spam filter allows for a .eml file to be passed in as a command line argument, then determines if it is spam or not using the Bayesian formula

#In the event that a new "learning process" is taking place, the generateDictionaries() call should be uncommented

#If the library files already exist, only functions from the Testing file will be called and the execution time will be drastically reduced

import sys
from Training import *
from Testing import *
from decimal import *

numHamEmails = 1077 #Total number of ham emails from learning phase
numSpamEmails = 1077 #Total number of spam emails from learning phase

if __name__ == "__main__":

    hamDictionary = []
    spamDictionary = []
    dictionaries = ()

    if (len(sys.argv) == 2):
        email = sys.argv[1]
    else:
        print "ERROR - Please provide .eml file"
        sys.exit()

#******************************************************************************************
    #generateDictionaries()                #ONLY CALL THIS IF CREATING NEW DICTIONARIES
#******************************************************************************************

    f = open('HAM_DICTIONARY', 'r')
    content = f.readlines()
    for line in content:
        hamDictionary.append(line)
    f.close

    f = open('SPAM_DICTIONARY', 'r')
    content = f.readlines()
    for line in content:
        spamDictionary.append(line)
    f.close


    spamicity = calcSpamicity(email, hamDictionary, spamDictionary, numHamEmails, numSpamEmails)

    print "spamicity = ",spamicity
    if (spamicity >= 70):
        print "message is spam"
    else:
        print "message is NOT spam"
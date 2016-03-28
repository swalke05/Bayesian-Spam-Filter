import sys
from Training import *
from Testing import *
from decimal import *

numHamEmails = 1721 #Total number of ham emails from learning phase
numSpamEmails = 779 #Total number of spam emails from learning phase

if __name__ == "__main__":


    dictionaries = ()

    if (len(sys.argv) == 2):
        email = sys.argv[1]
    else:
        print "ERROR - Please provide .eml file"
        sys.exit()


    dictionaries = generateDictionaries()
    hamDictionary = dictionaries[0]
    spamDictionary = dictionaries[1]

    # for item in hamDictionary:
    #     print item
    # print "between"
    # for item in spamDictionary:
    #     print item

    #chance = estimateClassContains("Guaranteed",hamDictionary, numHamEmails)
    #chance = estimateClassContains("",spamDictionary, numSpamEmails)
    #print chance

    spamicity = calcSpamicity(email, hamDictionary, spamDictionary, numHamEmails, numSpamEmails)
    print "spamicity = ",spamicity
    if (spamicity >= 80):
        print "message is spam"
    else:
        print "message is NOT spam"
    



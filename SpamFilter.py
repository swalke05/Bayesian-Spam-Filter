import sys
from Training import *
from Testing import *
from decimal import *

numHamEmails = 1721 #Total number of ham emails from learning phase
numSpamEmails = 779 #Total number of spam emails from learning phase

if __name__ == "__main__":
    dictionaries = ()

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

    spamicity = calcSpamicity("FREE", hamDictionary, spamDictionary, numHamEmails, numSpamEmails)
    print spamicity
    



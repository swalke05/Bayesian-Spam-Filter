import sys
from decimal import *

def estimateClassContains(word, dictionary, numEmails):
    estimate = -1
    i = 0
    for entry in dictionary:
        #print i
        i+=1
        #print entry[0]
        if (entry[0] == word):
            print entry[0], "appears", entry[1], "times in", numEmails, "emails"
            getcontext().prec = 3
            estimate = Decimal(entry[1])/Decimal(numEmails)
            break

    return estimate

def calcChanceHam(hamEstimate, spamEstimate):
    chanceHam = 0

    chanceHam = hamEstimate/(hamEstimate + spamEstimate)
    
    return chanceHam

#Assuming 50% chance any given message is spam/ham
def calcChanceSpam(hamEstimate, spamEstimate):
    chanceSpam = 0

    chanceSpam = spamEstimate/(hamEstimate + spamEstimate)

    return chanceSpam


def calcSpamicity(word, hamDictionary, spamDictionary, numHamEmails, numSpamEmails):
    spamicity = 0

    #Calculate P(word|ham)
    hamEstimate = estimateClassContains(word, hamDictionary, numHamEmails)
    print "hamEstimate = ",hamEstimate
    #Calculate P(word|spam)
    spamEstimate = estimateClassContains(word, spamDictionary, numSpamEmails)
    print "spamEstimate = ",spamEstimate
    #chanceHam = calcChanceHam(hamEstimate, spamEstimate)
    chanceSpam = calcChanceSpam(hamEstimate, spamEstimate)

    return chanceSpam





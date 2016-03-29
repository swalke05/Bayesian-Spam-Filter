import sys
from decimal import *
from Training import tokenizeFile
from operator import mul
import math

# Calculate P(word | spam)
def estimateClassContains(word, dictionary, numEmails):
    estimate = 0
    i = 0

    for entry in dictionary:
        #print i
        i+=1
        #print entry[0]
        if (entry[0] == word):
            print entry[0], "appears", entry[1], "times in", numEmails, "emails"
            if (entry[1] >= 0):
                getcontext().prec = 3
                estimate = Decimal(entry[1])/Decimal(numEmails)
                break
            else:
                estimate = 0

                break
    #if (estimate == 0):

        #print "less than 5 occurrences for", word

    return (estimate, entry[1])

def calcChanceHam(hamEstimate, spamEstimate):
    chanceHam = 0

    chanceHam = hamEstimate/(hamEstimate + spamEstimate)
    
    return chanceHam

#Assuming 50% chance any given message is spam/ham
#Calculate P(spam | word)
def calcChanceSpam(hamEstimate, spamEstimate):
    chanceSpam = 0
    # print hamEstimate
    # print spamEstimate
    chanceSpam = spamEstimate/(hamEstimate + spamEstimate)

    return chanceSpam

def calcSpamicity(email, hamDictionary, spamDictionary, numHamEmails, numSpamEmails):
    spamicity = 0
    numeratorList = []
    denominatorList = []
    allEmailWords = []
    emailWords = [] #no duplicates
    condensed = []
    info = ()
    keywords = []

    tokenizeFile(email, allEmailWords)

    emailWords = set(allEmailWords) #remove duplicates

    for word in emailWords:
        print (word)
        numOccurrences = 0
        #print "word in email:", word
        # #Calculate P(word|ham)

        info = estimateClassContains(word, hamDictionary, numHamEmails)
        hamEstimate = info[0]
        numOccurrences = info[1]

        print "hamEstimate = ",hamEstimate
        # #Calculate P(word|spam)
        info = estimateClassContains(word, spamDictionary, numSpamEmails)
        spamEstimate = info[0]
        numOccurrences += info[1]
        print "spamEstimate = ",spamEstimate

        #Less than 5 occurences in both datasets
        if (numOccurrences >= 5 and (hamEstimate != 0 and spamEstimate != 0)):
            chanceSpam = calcChanceSpam(hamEstimate, spamEstimate)
            if (len(numeratorList) >= 10):
                if ((abs(Decimal(0.5) - chanceSpam)) > (abs(Decimal(0.5) - (min(numeratorList))))):
                    print "absolute .5 -",chanceSpam, "=", abs(Decimal(0.5) - chanceSpam)
                    print "absolute .5 -",min(numeratorList), "=", abs(Decimal(0.5) - min(numeratorList) )
                    index = numeratorList.index(min(numeratorList))
                    numeratorList[index] = chanceSpam
                    denominatorList[index] = 1-chanceSpam
                    keywords[index] = word
            else:
                numeratorList.append(chanceSpam)
                denominatorList.append(1-chanceSpam)
                keywords.append(word)

    print "numerator"
    print numeratorList
    print "denominator" #remember to add numerator to denominator
    print denominatorList
    print keywords

    numerator = reduce(mul, numeratorList, 1)
    denominator = reduce(mul, denominatorList, 1) + numerator

    spamicity = (numerator/denominator)*100
    

        #chanceSpam = calcChanceSpam(hamEstimate, spamEstimate)
        #chanceHam = calcChanceHam(hamEstimate, spamEstimate)

    return spamicity





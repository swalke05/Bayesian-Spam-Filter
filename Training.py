#Training.py
#Spencer Walker
#0715530

#This file contains functions for the "learning" process of the spam filter
#When the generateDictionaries() function is called in main, this file is used to 
#Generate the dictionaries based on the label file to distinguish between ham/spam
#These functions are not called in the normal procedure of detecting spam (once dicttionary files exit)

import os
import sys
import re
import copy
from collections import Counter

def generateDictionaries():
    labelsFile = "training/SPAMTrain.label"
    hamLabels = []
    spamLabels = []
    hamFiles = []
    spamFiles = []
    hamCollection = []
    spamCollection = []
    hamWords = []
    spamWords = []
    path = "training/"

    parseLabels(labelsFile, hamLabels, spamLabels)
    splitFiles(hamLabels, spamLabels, hamFiles, spamFiles)

    #print "ham files"
    for file in hamFiles:
        #print file
        tokenizeFile(path+file[0], hamWords)
    #print "spam files"
    for file in spamFiles:
        #print file
        tokenizeFile(path+file[0], spamWords)

    hamCollection = Counter(hamWords).most_common()
    spamCollection = Counter(spamWords).most_common()

    f = open('HAM_DICTIONARY','w')
    for item in hamCollection:
        f.write(str(item)+"\n") 
    f.close()

    f = open('SPAM_DICTIONARY','w')
    for item in spamCollection:
        f.write(str(item)+"\n") 
    f.close() 

def tokenizeFile(file, dictionary):
    fileContents = ""

    with open(file) as f:
        content = f.readlines()

    for line in content:
        fileContents+=line

    words = re.findall(r"[\w']+", fileContents)

    for word in words:
        if (isWord(word)):
            if (len(word) > 4):
                dictionary.append(word)

def splitFiles(hamLabels, spamLabels, hamFiles, spamFiles):
    files = os.listdir('training/')

    for file in files:
        label = file.rsplit()
        if label == "Store":
            continue

        if (label in hamLabels):
            hamFiles.append(file.rsplit())
        elif (label in spamLabels):
            spamFiles.append(file.rsplit())

def parseLabels ( labelsFile, hamLabels, spamLabels ):
    with open(labelsFile) as f:
        content = f.readlines()

    for label in content:

        if (int(label.split(' ')[0]) == 0):
            spamLabels.append((label.split(' ')[1]).rsplit())
        else:
            hamLabels.append((label.split(' ')[1]).rsplit())

def isWord(word):
    if (word.lower() == "cellpadding"):
        return False
    elif(word.lower() == "debian"):
        return False
    elif(word.lower() == "width"):
        return False
    elif(word.lower() == "height"):
        return False
    elif(word.lower() == "lists"):
        return False
    elif(word.lower() == "border"):
        return False
    elif(word.lower() == "table"):
        return False
    elif(word.lower() == "bgcolor"):
        return False
    elif(word.lower() == "wrote"):
        return False
    elif(word.lower() == "email"):
        return False
    elif(word.lower() == "should"):
        return False
    elif(word.lower() == "could"):
        return False
    elif(word.lower() == "would"):
        return False
    elif(word.lower() == "about"):
        return False
    elif(word.lower() == "there"):
        return False
    elif(word.lower() == "don't"):
        return False
    elif(word.lower() == "can't"):
        return False
    elif(word.lower() == "won't"):
        return False
    elif(word.lower() == "their"):
        return False
    elif(word == "000000"):
        return False
    elif(word.lower() == "align"):
        return False
    elif(word.lower() == "right"):
        return False
    elif(word.lower() == "Arial"):
        return False
    elif(word.lower() == "_______________________________________________"):
        return False
    elif(word.lower() == "still"):
        return False
    elif(word.lower() == "arial"):
        return False
    elif(word.lower() == "helvetica"):
        return False
    elif(word.lower() == "since"):
        return False
    elif(word.lower() == "these"):
        return False
    elif(word.lower() == "really"):
        return False
    elif(word.lower() == "serif"):
        return False
    elif(word.lower() == "colspan"):
        return False
    elif(word.lower() == "https"):
        return False
    elif(word.lower() == "center"):
        return False
    elif(word.lower() == "_blank"):
        return False
    elif(word.lower() == "without"):
        return False
    elif(word.lower() == "doesn't"):
        return False
    elif(word.lower() == "through"):
        return False
    elif(word.lower() == "actually"):
        return False
    elif(word.lower() == "ffffff"):
        return False
    elif(word.lower() == "charset"):
        return False
    elif(word.lower() == "color"):
        return False
    elif(word.lower() == "style"):
        return False
    elif(word.lower() == "style"):
        return False
    elif(word.lower() == "family"):
        return False
    elif(word.lower() == "decoration"):
        return False
    elif(word.lower() == "background"):
        return False
    elif (word.lower() == "cellspacing"):
        return False
    elif (word.lower() == "valign"):
        return False
    elif (word.lower() == "version"):
        return False
    elif (word.lower() == "content"):
        return False
    elif (word.lower() == "where"):
        return False
    elif (word.lower() == "target"):
        return False
    elif (word.lower() == "default"):
        return False
    elif (word.lower() == "cellspacing"):
        return False
    elif (word.lower() == "you'll"):
        return False
    elif (word.lower() == "vertical"):
        return False
    elif (word.lower() == "horizontal"):
        return False

    else:
        return True

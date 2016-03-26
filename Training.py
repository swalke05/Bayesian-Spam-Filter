#Training.py
#Spencer Walker
#0715530

import os
import sys

def generateDictionary(hamDictionary, spamDictionary):
    labelsFile = "spam-mail.tr.label"
    hamLabels = []
    spamLabels = []
    hamFiles = []
    spamFiles = []

    parseLabels(labelsFile, hamLabels, spamLabels)
    splitFiles(hamLabels, spamLabels, hamFiles, spamFiles)

    for file in hamFiles:
        tokenizeFile("training/"+file, hamDictionary)

    #tokenizeFile(spamFiles, spamDictionary)

def tokenizeFile(file, dictionary):
    with open(file) as f:
        content = f.readlines()

    for line in content:
        words = line.split(' ')
        for word in words:
            print word

def splitFiles(hamLabels, spamLabels, hamFiles, spamFiles):
    files = os.listdir('training')

    for file in files:
        label = (file.split('_')[1]).split('.')[0]
        if (label in hamLabels):
            hamFiles.append(file)
        else:
            spamFiles.append(file)



def parseLabels ( labelsFile, hamLabels, spamLabels ):
    with open(labelsFile) as f:
        content = f.readlines()

    for label in content:
        if (int(label.split(',')[1]) == 0):
            spamLabels.append(label.split(',')[0])
        else:
            hamLabels.append(label.split(',')[0])

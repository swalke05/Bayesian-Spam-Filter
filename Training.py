#Training.py
#Spencer Walker
#0715530

import os
import sys
import re
from collections import Counter

def generateDictionary(hamDictionary, spamDictionary):
    labelsFile = "spam-mail.tr.label"
    hamLabels = []
    spamLabels = []
    hamFiles = []
    spamFiles = []
    hamCollection = []

    parseLabels(labelsFile, hamLabels, spamLabels)
    splitFiles(hamLabels, spamLabels, hamFiles, spamFiles)

    for file in hamFiles:
        tokenizeFile("training/"+file, hamDictionary)
    for file in spamFiles:
        tokenizeFile("training/"+file, spamDictionary)

    hamCollection = Counter(hamDictionary).most_common()
    spamCollection = Counter(spamDictionary).most_common()

    hamDictionary = hamCollection
    spamDictionary = spamCollection

def tokenizeFile(file, dictionary):
    fileContents = ""

    with open(file) as f:
        content = f.readlines()

    for line in content:
        fileContents+=line

    words = re.findall(r"[\w']+", fileContents)

    for word in words:
        dictionary.append(word)

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

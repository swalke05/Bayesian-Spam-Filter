#Training.py
#Spencer Walker
#0715530

import os
import sys
import re
import copy
from collections import Counter

def generateDictionaries():
    labelsFile = "spam-mail.tr.label"
    hamLabels = []
    spamLabels = []
    hamFiles = []
    spamFiles = []
    hamCollection = []
    spamCollection = []
    hamWords = []
    spamWords = []

    parseLabels(labelsFile, hamLabels, spamLabels)
    splitFiles(hamLabels, spamLabels, hamFiles, spamFiles)

    for file in hamFiles:
        tokenizeFile("training/"+file, hamWords)
    for file in spamFiles:
        tokenizeFile("training/"+file, spamWords)

    hamCollection = Counter(hamWords).most_common()
    spamCollection = Counter(spamWords).most_common()

    return (hamCollection,spamCollection)

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

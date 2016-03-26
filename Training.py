#Training.py
#Spencer Walker
#0715530

import os
import sys

def parseLabels ( labelsFile, hamFiles, spamFiles ):
    with open(labelsFile) as f:
        content = f.readlines()

    for label in content:
        print label.split(',')[1]
        if (int(label.split(',')[1]) == 0):
            spamFiles.append(label.split(',')[0])
        else:
            hamFiles.append(label.split(',')[0])

labelsFile = "spam-mail.tr.label"
hamFiles = []
spamFiles = []

parseLabels(labelsFile, hamFiles, spamFiles)

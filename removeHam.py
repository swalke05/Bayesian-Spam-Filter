#Spencer Walker

#Simple tool to remove ham files from the training set to have equal number of ham/spam messages in order
#to achieve an unbiased dataset
import email.parser 
import os, sys, stat
import shutil

with open("dataset2/SPAMTrain.label") as f:
    content = f.readlines()

    i = 0
    for label in content:
        if (i == 1571):
            print "reached max files"
            break


        if (int(label.split(' ')[0]) == 1):

            path = label.split(' ')[1]
            path = path.rstrip()
            print (path)

            if (os.path.isfile("./dataset2/TRAINING/"+path)):
                print("path exists")
                os.rename("./dataset2/TRAINING/"+path, "./removed/"+path)
                i +=1
            else:
                print "dataset2/TRAINING/"+path, "is not a file"
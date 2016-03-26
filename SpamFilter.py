import sys
from Training import *
from Testing import *
from decimal import *

if __name__ == "__main__":
    dictionaries = ()

    dictionaries = generateDictionaries()
    hamDictionary = dictionaries[0]
    spamDictionary = dictionaries[1]

    chance = getChanceHamContains("password",hamDictionary)
    print chance
    



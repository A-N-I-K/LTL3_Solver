'''
Created on Feb 16, 2020

@author: Anik
'''

import re
import time
from z3 import *

pathToGraphDir = "digraphs/"


def getStates():
    
    return


def getLabel():
    
    return


def getLTL3(fileName):
    
    ltl3 = []
    path = pathToGraphDir + fileName
    
    file = open(path)
    
    line = file.readline()
    ltl3.append(line.rstrip())
    
    while line:
        
        line = file.readline()
        ltl3.append(line.rstrip())
        
    file.close()
    
    return ltl3


def main():
    
    testFile = "a U b.txt"
    print(getLTL3(testFile))


if __name__ == '__main__':
    
    start = time.time()
    
    main()
    
    print("Terminated..")
    print("Time elapsed :", (time.time() - start), "seconds")
    
    pass

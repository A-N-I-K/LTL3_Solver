'''
Created on Feb 16, 2020

@author: Anik
'''

import time
from z3 import *

pathToGraphDir = "digraphs/"


def getLTL3(fileName):
    
    path = pathToGraphDir + fileName
    
    # s = Solver()
    
    file = open(path)
    line = file.readline()
    
    while line:
        
        # param = line.split("\t")
        
        line = file.readline()
        print(line)
        
    file.close()
    
    return


def main():
    
    testFile = "a U b.txt"
    getLTL3(testFile)


if __name__ == '__main__':
    
    start = time.time()
    
    main()
    
    print("Terminated..")
    print("Time elapsed :", (time.time() - start), "seconds")
    
    pass

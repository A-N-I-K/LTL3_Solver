'''
Created on Feb 16, 2020

@author: Anik
'''

import re
import time

from z3 import *

pathToGraphDir = "digraphs/"
stateMapper = {}


def populateMapper(lines):

    for line in lines:

        stateFrom, stateTo, isLoop = getStates(line)
        stateLabel = getLabel(line)
        
        if (stateFrom != None or  stateTo != None or stateLabel != None):

            # stateMapper[stateFrom] = []

            stateMapper[stateFrom].append([stateTo, stateLabel])


def createStatesInMapper(lines):

    for line in lines:

        try:

            match = re.compile("\"\(.*\)\" \[label=\"\(")
            label = match.findall(line)[0][2:-12]

            stateMapper[label] = []

        except:

            # print("Given line :", line, "could not be parsed.")
            pass


def getStates(line):
    
    # print(line)

    try:

        match = re.compile("\(.*\)\" -> \"\(")
        stateFrom = match.findall(line)[0][1:-8]

        match = re.compile("\)\" -> \"\(.*\)\" \[label = \"\(")
        stateTo = match.findall(line)[0][8:-14]

        return stateTo, stateFrom, stateTo == stateFrom

    except:

        # print("Given line :", line, "could not be parsed.")
        return None, None, False


def getLabel(line):

    # print(line)

    try:
        
        match = re.compile("\)\" \[label = \"\(.*\)\"\]")
        label = match.findall(line)[0][14:-3]

        return label

    except:

        # print("Given line :", line, "could not be parsed.")
        return None


def getLTL3(fileName):
    
    ltl3 = []
    path = pathToGraphDir + fileName
    
    file = open(path)
    
    line = file.readline()
    
    while line:
        
        line = file.readline()
        ltl3.append(line.rstrip())
        
    file.close()
    
    return ltl3


def main():
    
    testFile = "a U b.txt"

    ltl3 = getLTL3(testFile)
    # print(populateMapper(ltl3[0]))

    createStatesInMapper(ltl3)
    populateMapper(ltl3)

    # print(createStatesInMapper(ltl3))

#     mapper = {}
#     s = []
#     s.append("aj")
#
#     mapper["anik"] = []
#     mapper["anik"].append("ax")
#     mapper["anik"].append("ab")

    print(stateMapper)


if __name__ == '__main__':
    
    start = time.time()
    
    main()
    
    print("Terminated..")
    print("Time elapsed :", (time.time() - start), "seconds")
    
    pass

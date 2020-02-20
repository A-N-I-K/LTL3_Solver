'''
Created on Feb 16, 2020

@author: Anik
'''

import re
import time

from z3 import *

pathToGraphDir = "digraphs/"
stateMapper = {}

stateStart = []
stateAccept = []
stateReject = []


def markStartState():

    # print(stateMapper)

    # backtrack from accept state
    startStateFromAcc = stateAccept[0]

    # print(stateMapper[startStateFromAcc])

    while(True):

        for state in stateMapper[startStateFromAcc]:
            # print("outer", state)

            if (state[0] != startStateFromAcc) & (len(state) == 2):
                
                startStateFromAcc = state[0]
                # print(state[0])

        break


def populateMapper(lines):
    
    print(stateMapper)

    for line in lines:

        stateFrom, stateTo, isLoop = getStates(line)
        stateLabel = getLabel(line)
        
        print(stateTo, stateFrom, line)
        
        if (stateFrom != None or  stateTo != None or stateLabel != None):

            # stateMapper[stateFrom] = []
            stateMapper[stateTo].append([stateFrom, stateLabel])
            
            # print(stateMapper)

    markStartState()


def createStatesInMapper(lines):

    for line in lines:

        if ")\", style=filled, color=" in line:

            try:

                match = re.compile("\"\(.*\)\" \[label=\"\(")
                label = match.findall(line)[0][2:-12]

                if "green" in line:

                    stateMapper[label] = [["accept"]]
                    stateAccept.append(label)

                if "red" in line:

                    stateMapper[label] = [["reject"]]
                    stateReject.append(label)

                if "yellow" in line:

                    stateMapper[label] = [["unknown"]]

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
        
        # print(stateFrom, stateTo)

        return stateFrom, stateTo, stateTo == stateFrom

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

    # print(stateMapper)


if __name__ == '__main__':
    
    start = time.time()
    
    main()
    
    print("Terminated..")
    print("Time elapsed :", (time.time() - start), "seconds")
    
    pass

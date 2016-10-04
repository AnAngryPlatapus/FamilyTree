#!/usr/bin/python

import sys
file_name = sys.argv[1]

family = [] #family["Luke"] = ["Name", [Parents], [Children], [Spouses]] If parents are blank, no more ancestors. If children blank, last people.

def searchAncestors(pivotPerson, targetPerson, family):
    if(not family[pivotPerson][1]):
        return False
    if(targetPerson in family[pivotPerson][1]):
        return True
    for person in family[pivotPerson][1]:
        if(searchAncestors(person,targetPerson,family)):
            return True
    return False
def addAncestor(person, family, ancestors):
    ancestors.append
def commonAncestor(pivotPerson, targetPerson, family):
    ancestors=[]
    for person in family[pivotPerson][1]:
        addAncestor(person)

output = open("output.txt",w)
with open(file_name) as f:
    for line in f:
        lineArguements = line.split()
        if(lineArguements[0]=="E"):
            if(lineArguements[1] in family):
                family[lineArguements[1]][3].append(lineArguements[2])
            else:
                family[lineArguements[1]]=[lineArguements[1],[],[],[lineArguements[2]]]
            if(lineArguements[2] in family):
                family[lineArguements[2]][4].append(lineArguements[1])
            else:
                family[lineArguements[2]]=[lineArguements[2],[],[],[lineArguements[1]]]
            if(len(lineArguements)>3):
                family[lineArguements[1]][2].append(lineArguements[3])
                family[lineArguements[2]][2].append(lineArguements[3])
                if(lineArguements[3] in family):
                    family[lineArguements[3]][1].append(lineArguements[1])
                    family[lineArguements[3]][1].append(lineArguements[2])
                else:
                    family[lineArguements[3]]=[lineArguements[3],[lineArguements[1],lineArguements[2]],[],[]]
        elif(lineArguements[0]=="R"):
            pivotPerson=lineArguements[1]
            targetPerson=lineArguements[2]
            if(targetPerson in family[pivotPerson][3]):
                output.write(targetPerson+" and "+pivotPerson+" are spouses.\n")
            elif(targetPerson in family[pivotPerson][1]):
                output.write(targetPerson+" is the parent of "+pivotPerson+".\n")
            elif(targetPerson in family[pivotPerson][2]):
                output.write(pivotPerson+" is the parent of "+targetPerson+".\n")
            elif(targetPerson[1][0] in pivotPerson[1] & targetPerson[1][1] in pivotPerson[1]):
                output.write(pivotPerson+" and "+targetPerson+" are siblings.\n")
            elif(targetPerson[1][0] in pivotPerson[1] | targetPerson[1][1] in pivotPerson[1]): #do not need to check if not full siblings as that happens above
                output.write(pivotPerson+" and "+targetPerson+" are half-siblings.\n")
            elif(searchAncestors(pivotPerson,targetPerson,family)):
                output.write(targetPerson+" is an ancestor of "+pivotPerson+".\n")
            elif(searchAncestors(targetPerson,pivotPerson,family)):
                output.write(pivotPerson+" is an ancestor of "+searchPerson+".\n")
            elif(commonAncestor(targetPerson, pivotPerson, family)):  #check if both have common ancestor

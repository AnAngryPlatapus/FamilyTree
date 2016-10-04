elif(lineArguments[0]=="X"):
    pivotPerson=lineArguments[1]
    targetPerson=lineArguments[3]
    if (lineArguments[2]=="spouse"):
        if (targetPerson in family[pivotPerson][3]):
            print("True")
        else:
            print("False")
    elif(lineArguments[2]=="parent"):
        if  (targetPerson in family[pivotPerson][1]):
            print("True")
        else:
            print("False")
    elif(lineArguments[2]=="sibling"):
        if (targetPerson[1][0] in pivotPerson[1] & targetPerson[1][1] in pivotPerson[1]):
            print("True")
        else:
            print("False")
    elif(lineArguments[2]=="half-sibling"):
        if ((targetPerson[1][0] in pivotPerson[1] & targetPerson[1][1] not in pivotPerson[1])|(targetPerson[1][0]not in pivotPerson[1]& targetPerson[1][1] in pivotPerson[1])):
            print("True")
        else:
            print("False")
    elif(lineArguments[2]=="ancestor"):
        if (searchAncestors(targetPerson, pivotPerson, family):
            print("True")
        else:
            print("False")


def oneEditAway(string1, string2):
    if len(string1) == len(string2):
        return oneReplaceAway(string1, string2)
    elif len(string1) + 1 == len(string2):
        return oneInsertAway(string1, string2)
    elif len(string1) == len(string2) + 1:
        return oneInsertAway(string2, string1)
    
    return False


def oneInsertAway(string1, string2):
    index1 = 0
    index2 = 0
    foundDifference = False
    while index1 < len(string1):
        if string1[index1] != string2[index2]:
            if foundDifference:
                return False
            else:
                foundDifference = True
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    
    return True
   
    
def oneReplaceAway(string1, string2):
    foundDifference = False
    for i in range(len(string1) - 1):
        if string1[i] != string2[i]:
            if foundDifference:
                return False
            else:
                foundDifference = True
    return True


print(oneEditAway("test", "testt"))
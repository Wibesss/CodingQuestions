from collections import Counter

def getDiffInLetters(hs1, hs2):
    diffLetters = 0
    for key in hs1.keys():
        if key not in hs2.keys():
            diffLetters +=1
    return diffLetters

def oneEditAway(string1, string2):
    if string1 == string2:
        return True
    
    diffInLength = abs(len(string1) - len(string2))
    if diffInLength > 1:
        return False
    
    letterCount1 = Counter(string1)
    letterCount2 = Counter(string2)
    
    diffInLetters = 0
    if letterCount1.keys() > letterCount2.keys():
        diffInLetters = getDiffInLetters(letterCount1, letterCount2)
    else:
        diffInLetters = getDiffInLetters(letterCount2, letterCount1)
        
    if diffInLetters > 1:
        return False
    
    if diffInLength == 1:
        if diffInLetters == 1:
            return True
        else:
            return False
    else:
        return True
     
            
print(oneEditAway("jeste", "jest"))           
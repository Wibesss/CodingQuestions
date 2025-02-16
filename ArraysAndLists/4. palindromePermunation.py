from collections import Counter

# String has to have maximum of 1 characters that occur only once 
def palindromePermutations(string):
    hm = Counter(string)
    numOfSingleLetters = 0
    for key in hm.keys():
        if key != " " and hm[key] % 2 == 1:
            numOfSingleLetters += 1
        if numOfSingleLetters > 1:
            return False
    return True

    
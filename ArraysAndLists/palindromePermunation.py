from collections import Counter

def palindromePermutations(string):
    hm = Counter(string)
    numOfSingleLetters = 0
    for key in hm.keys():
        if key != " " and hm[key] % 2 == 1:
            numOfSingleLetters += 1
        if numOfSingleLetters > 1:
            return False
    return True

    
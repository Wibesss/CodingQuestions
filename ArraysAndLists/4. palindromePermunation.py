from collections import Counter

# Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. A permutationis a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words. 

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

    
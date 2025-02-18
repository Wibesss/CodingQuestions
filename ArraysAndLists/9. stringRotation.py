
# Assume you have a method isSubstring which checks if oneword is a substring of another. 
# Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring 
# (e.g., "waterbottle" is a rotation of"erbottlewat"). 

# Using "in" operator as an implementation of the isSsubrsting
def stringRotation(string1, string2):
    return string2 in string1+string1


print(stringRotation("jeste", "estej"))
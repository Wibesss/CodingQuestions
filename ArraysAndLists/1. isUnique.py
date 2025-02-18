
# Implement an algorithm to determine if a string has all unique characters. What if youcannot use additional data structures?

def isUnique(string):
    s = set()
    for char in string:
        if char in s:
            return False
        s.add(char)
    return True


def isUniqueNoDS(string):
    sorted_str = sorted(string)
    for i in range(len(sorted_str) - 1):
        if sorted_str[i] == sorted_str[i + 1]:
            return False
    return True



from collections import Counter

# O(N) time, O(N) space
def isPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    hs = Counter(string2)
    for char in string1:
        if hs[char] > 0:
            hs[char] -= 1
        else:
            return False
    return True

# O(N log N) time, O(1) space
def isPermutationNoDS(string1, string2):
    if len(string1) != len(string2):
        return False
    return sorted(string1) == sorted(string2)


import unittest

class TestIsPermutation(unittest.TestCase):
    def test_permutations(self):
        self.assertTrue(isPermutation("abc", "bca"))
        self.assertTrue(isPermutation("12345", "54321"))
        self.assertTrue(isPermutation("aabbcc", "bbaacc"))
        self.assertTrue(isPermutation("", ""))

    def test_not_permutations(self):
        self.assertFalse(isPermutation("abc", "ab"))
        self.assertFalse(isPermutation("hello", "helloo"))
        self.assertFalse(isPermutation("abcd", "abce"))
        self.assertFalse(isPermutation("apple", "aplee"))

if __name__ == "__main__":
    unittest.main()

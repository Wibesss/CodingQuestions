
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

import unittest

class TestIsUnique(unittest.TestCase):
    def test_unique_strings(self):
        self.assertTrue(isUnique("abcde"))
        self.assertTrue(isUnique("AaBbCc"))
        self.assertTrue(isUnique(""))

    def test_non_unique_strings(self):
        self.assertFalse(isUnique("hello"))
        self.assertFalse(isUnique("apple"))
        self.assertFalse(isUnique("123321"))

    def test_unique_strings_no_ds(self):
        self.assertTrue(isUniqueNoDS("abcde"))
        self.assertTrue(isUniqueNoDS("AaBbCc"))
        self.assertTrue(isUniqueNoDS(""))

    def test_non_unique_strings_no_ds(self):
        self.assertFalse(isUniqueNoDS("hello"))
        self.assertFalse(isUniqueNoDS("apple"))
        self.assertFalse(isUniqueNoDS("123321"))

if __name__ == "__main__":
    unittest.main()


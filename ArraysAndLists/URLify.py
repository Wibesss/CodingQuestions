def URLify(string):
    
    sl = list(string)
    
    for i in range(len(sl) - 1):
        if sl[i] == " ":
            for j in range(len(sl) - 1, i+2, -1):
                sl[j]=sl[j-2]
            sl[i]="%"
            sl[i+1]="2"
            sl[i+2]="0"
            
    return "".join(sl)


import unittest

class TestURLify(unittest.TestCase):
    def test_regular_strings(self):
        self.assertEqual(URLify("Mr John Smith    "), "Mr%20John%20Smith")  # 2 spaces at the end for '%20'
        self.assertEqual(URLify("Hello World  "), "Hello%20World")  # 1 space at the end

    def test_leading_trailing_spaces(self):
        self.assertEqual(URLify("  Mr John Smith        "), "%20%20Mr%20John%20Smith")  # Leading space + 3 spaces at the end
        self.assertEqual(URLify("  Hello    "), "%20%20Hello")  # Leading space, 1 extra at the end

    def test_multiple_spaces(self):
        self.assertEqual(URLify("A  B  C        "), "A%20%20B%20%20C")  # Each space replaced, extra spaces at the end

    def test_empty_string(self):
        self.assertEqual(URLify(""), "")

    def test_no_spaces(self):
        self.assertEqual(URLify("NoSpacesHere"), "NoSpacesHere")  # No spaces to replace

if __name__ == "__main__":
    unittest.main()


              
            
            

# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2blc5a3. 
# If the "compressed" string would not become smaller than the original string, your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z).

def stringCompressor(string):
    newString = []
    index = 0
    count = 0
    while index < len(string):      
        count += 1
        if index == len(string) - 1 or string[index] != string[index + 1]:
            newString.append(string[index])
            newString.append(str(count))
            count = 0
        index += 1
    return "".join(newString) if len(newString) < len(string) else string
            
            
print(stringCompressor("aabcccccaaa"))
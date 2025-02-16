
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

# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.

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

              
            
            
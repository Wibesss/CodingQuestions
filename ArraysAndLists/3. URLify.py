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

              
            
            
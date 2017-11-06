s = 'nddbtasnacgsltzgfnbqsbg'
long = ''                    #store longest substring
for i in range(len(s)-1):   # so that while loop can be performed without getting string index out of range
    temp = ''              #store current longest substring
    start = i             #starting position for substring
    temp += s[start]
    while ord(s[start+1])>=ord(s[start]):
        temp += s[start+1]
        if start+1==len(s)-1:  #if start+1 is at end of string, there will be no use for while loop
            break
        start += 1
    if len(long)<len(temp):
        long = temp
print ('Longest substring in alphabetical order is:', long)
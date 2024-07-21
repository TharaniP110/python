string=input()
length=len(string)
for i in range (0,length):
    print(string[i+1:]+string[:i+1])

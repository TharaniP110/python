def func(n):
    count=1
    string=""
    for i in range (0,n):
        string=string+str(count)+""
        count+=1
    return string
n=int(input())
result=func(n)
print(result)

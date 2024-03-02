def multiply(n):
    if n==1:
        return 1
    else:
        return (n*multiply(n-1))
        
n=int(input())
result=multiply(n)
print(result)

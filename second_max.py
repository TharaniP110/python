n = int(input())
arr = map(int, input().split())
largest=second_largest=float('-inf')
for i in arr:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!= largest:
        second_largest=i
        
print(second_largest)

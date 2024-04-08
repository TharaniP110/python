s1=input()
s2=input()
s2_index=0
for i in s1:
    if i==s2[s2_index]:
        s2_index += 1
    if  s2_index==len(s2):
        break
if s2_index==len(s2):
    print("Yes")
else:
    print("No")
        

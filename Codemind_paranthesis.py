n=input()
res=''
c=0
for i in n:
    if i=='(':
        c+=1
        if c>1:
            res+=i
    if i==')':
        if c>1:
            res+=i
        c-=1
print(res)

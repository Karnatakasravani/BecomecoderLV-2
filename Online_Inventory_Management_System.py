n=int(input())
k=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i==k:
        l.append(1)
    else:
        l.append(-1)
print(max(l))

n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(len(arr)-1):
    if arr[i+1]<arr[i]:
        l.append(arr[i+1])
    else:
        l.append(-1)
l.append(-1)
print(*l)

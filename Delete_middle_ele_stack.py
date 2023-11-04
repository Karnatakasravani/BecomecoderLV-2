n=int(input())
if n%2==0:
    x=(n//2)-1
else:
    x=n//2
m=[]
a=list(map(int,input().split()))
for i in range(n):
    if i!=x:
        print(a[i],end=" ")

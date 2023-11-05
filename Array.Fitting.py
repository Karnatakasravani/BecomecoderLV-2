n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
c=0
for i in range(n):
    if b[i]<a[i]:
        print("NO")
        c=1
        break
if c==0:
    print("YES")

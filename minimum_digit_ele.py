n=int(input())
a=list(map(int,input().split()))
x=[]
for i in a:
    x.append(len(str(i)))
print(x.count(min(x)))

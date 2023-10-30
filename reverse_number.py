n=int(input())
if n<0:
    m=-n
else:
    m=n
P=str(m)[::-1]
p=int(P)
if n<0:
    print(-p)
else:
    print(p)

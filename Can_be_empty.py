t=int(input())
for i in range(1,t+1):
    n=input()
    x=n.count('A')
    y=n.count('B')
    z=n.count('C')
    if y==(x+z):
        print("YES")
    else:
        print("NO")

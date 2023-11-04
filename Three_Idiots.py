t=int(input())
for i in range(1,t+1):
    a,b,c=map(int,input().split())
    if a+b==abs(c) or b+c==abs(a) or a+c==abs(b):
        print("YES")
    else:
        print("NO")

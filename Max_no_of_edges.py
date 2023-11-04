t=int(input())
for _ in range(1,t+1):
    a,b,c=map(int,input().split())
    res=(a*(a-1)//2)-(b*(b-1)//2)-(c*(c-1)//2)
    print(res)

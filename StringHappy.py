n=input()
k=input()
m=int(input())
cnt=0
for i in n:
    if i==k:
        cnt+=1
if cnt>=m:
    print("1")
else:
    print("0")

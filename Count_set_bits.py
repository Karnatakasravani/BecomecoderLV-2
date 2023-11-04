for i in range(int(input())):
    x=int(input())
    n=bin(x)[2::]
    print(n.count('1'))

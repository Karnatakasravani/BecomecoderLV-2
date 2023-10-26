n=input()
v=0
c=0
d=0
s=0
n=n.lower()
for i in n:
    if i.isalpha():
        if i in "aeiou":
            v+=1
        else:
            c+=1
    elif i.isdigit():
        d+=1
    else:
        s+=1
print("Vowels: %d\nConsonants: %d\nDigits: %d\nWhite spaces: %d"%(v,c,d,s))

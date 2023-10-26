def rev_equ(s):
    oper="+-*/"
    component=[]
    curr_comp=""
    for i in s:
        if i in oper:
            component.append(curr_comp)
            component.append(i)
            curr_comp=""
        else:
            curr_comp+=i
    component.append(curr_comp)
    rev_equ=''.join(component[::-1])
    return rev_equ
s=input()
rev_equ=rev_equ(s)
print(rev_equ)

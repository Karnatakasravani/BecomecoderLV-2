n = input()
n = n.lower()
A = set('abcdefghijklmnopqrstuvwxyz')
N = set(n)
missing_set = A - N
missing_letters = ''.join(sorted(missing_set))
if missing_letters!=0:
    print(missing_letters)
else:
    print(0)

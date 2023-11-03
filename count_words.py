#start with vowel and ends with consonent
s=input()
words = s.split()
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = set('bcdfghjklmnpqrstvwxyz')
cnt = 0
for word in words:
    if len(word) > 1 and word[0].lower() in vowels and word[-1].lower() in consonants:
        cnt += 1
print(cnt)

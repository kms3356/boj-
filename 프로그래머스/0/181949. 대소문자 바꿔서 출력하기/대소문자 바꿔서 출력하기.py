str = input()
res = []
for s in str:
    if s.isupper():
        res.append(s.lower())
    else:
        res.append(s.upper())
print(''.join(res))
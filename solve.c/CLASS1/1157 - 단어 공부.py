sentence = input()

alpha = dict()

for x in sentence:
    if x.islower():
        x = x.upper()
    if x not in alpha:
        alpha[x] = 1
    else:
        alpha[x] += 1

maxcnt = max(alpha.values())
# print(maxcnt)

answer= []
for key, value in alpha.items():
    if value == maxcnt:
        answer.append(key)

if len(answer)!=1:
    print('?')
else:
    print(answer[0])
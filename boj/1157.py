word = str(input())

alphabet = {}
for alpha in [chr(x) for x in range(ord('A'), ord('Z') + 1)] + [chr(x) for x in range(ord('a'), ord('z') + 1)]:
  alphabet.setdefault(alpha, 0)

for w in word:
    if str(w) >= 'a':
      alphabet[w.upper()] += 1
    else:
      alphabet[w] += 1

alphabet = sorted(alphabet.items(), key=lambda item: item[1])

if alphabet[-1][1] == alphabet[-2][1]:
   print('?')
else:
   print(alphabet[-1][0])
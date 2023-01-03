import sys
alphabet = [0] * 26 # [0(a),0,0,0,0...0(z)]
for line in sys.stdin:
  chrs = list(str(line).strip())
  for c in chrs:
    if c != ' ' and c != '\0':
      alphabet[ord(c)-97]+=1
maxValue = max(alphabet)
maxAlpha = [alphabet.index(maxValue)]
for idx in range (len(alphabet)):
  if maxValue == alphabet[idx]:
    maxAlpha.append(idx)
print(''.join(list(map(lambda v: chr(v+97),(sorted(set(maxAlpha)))))))
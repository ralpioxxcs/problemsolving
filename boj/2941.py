alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
count = 0
i = 0
while i < len(str(word)):
  count += 1
  if i <= len(str(word)) - 3 and word[i] + word[i + 1] + word[i + 2] in alpha:
    i += 3
  elif i <= len(str(word)) - 2 and word[i] + word[i + 1] in alpha:
    i += 2
  else:
    i += 1
print(count)
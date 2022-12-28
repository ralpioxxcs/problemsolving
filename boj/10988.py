word = list(str(input()))
idx = 0
for idx in range(len(word)-1):
  if word[idx] != word[len(word)-1-idx]:
    print(0)
    exit(0)
print(1)
while True:
  no = False
  pal = list(str(input()))
  if pal[0] == '0':
    break
  for i in range(len(pal)-1):
    if pal[i] != pal[(len(pal)-1)-i]:
      print("no")
      no = True
      break
  if not no:
    print("yes")
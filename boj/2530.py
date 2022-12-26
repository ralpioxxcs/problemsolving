h, m, s = map(int, input().split())
ts = int(input())
h = (h + (m + (ts//60) + ((s + ts % 60) // 60))//60) % 24
m = (m + (ts//60) + ((s + ts % 60) // 60)) % 60
s = (s + ts % 60) % 60
print("{} {} {}".format(h, m, s))

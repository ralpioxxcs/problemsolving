t = []
while 1:
    v = float(input())
    if v == 999: break
    t.append(v)
for v in range(1, len(t)):
    print("%.2f" % (float(t[v])-float(t[v-1])))

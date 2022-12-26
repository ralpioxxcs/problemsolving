N = int(input())
count = 0

def isSeq(n):
    Nstr = list(map(str,str(n)))
    if len(Nstr) <= 2:
        return True
    else:
        diff = int(Nstr[1]) - int(Nstr[0])
        for v in range(2, len(Nstr)):
            diff2 = int(Nstr[v]) - int(Nstr[v-1])
            if diff != diff2:
                return False

    return True

for i in range(1,N+1):
    if(isSeq(i)):
        count += 1
print(count)
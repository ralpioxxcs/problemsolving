n = int(input())

def solve(num):
    # ex) num : 10
    # '1','0'
    # '0'
    ans.append(num)
    lastNum = int(str(num)[-1])

    # decremental number
    for i in range(lastNum):
        numStr = str(num) + str(i)
        solve(int(numStr))

if n > 1023:
    print(-1)
else:
    ans = []
    for i in range(10):
        solve(i)
    print(sorted(ans)[n-1])
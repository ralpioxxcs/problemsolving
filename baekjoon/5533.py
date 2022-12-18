N = int(input())
score = [[0 for j in range(3)] for i in range(N)]
finalScore = []
for i in range(N):
    finalScore.append(0)

# input
for i in range(N):
    a,b,c = map(int,input().split())
    score[i][0] = a
    score[i][1] = b
    score[i][2] = c

for i in range(3):
    # setup score
    gameScore = []
    for j in range(N):
        gameScore.append(score[j][i])

    for ii in range(0, N):
        zero = False
        for jj in range(0,N):
            if ii == jj: continue
            if(gameScore[ii] == gameScore[jj]):
                finalScore[ii] += 0
                zero = True
                break

        if(zero != True):
            finalScore[ii] += gameScore[ii]

for i in finalScore:
    print(i)

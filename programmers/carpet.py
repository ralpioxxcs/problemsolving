def solution(brown, yellow):
    answer = []

    # brown:  0
    # yellow: 1

    for n in range(2, brown):
        carpet = []

    	# n 크기의 사각형 윗 변(갈색) 삽입
        carpet.append([0] * n)

        height = 0
        while height < n-2:
    		# 내부 채우기
            carpet.append([0] * n)
       	    # 아랫 변
            carpet.append([0] * n)

            if brown + yellow == len(carpet) * n:
                answer = [n, len(carpet)]
                return answer
            else:
                carpet.pop()
                
            height += 1

    return answer

#=============================================================================

def solution(brown, yellow):
    answer = []

    # brown:  2w + 2h - 4
    # yellow: (w-2) * (h-2)
    
    for w in range(1, brown):
        for h in range(w+1):
            if (2*w + 2*h - 4) == brown and (w-2) * (h-2) == yellow:
                answer = [w,h]
                return answer

    return answer

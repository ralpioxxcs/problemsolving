def solution(data, col, row_begin, row_end):
    answer = 0

    # col번째 인덱스 기준 오름차순 정렬
    #for i in range(0, len(data) - 1):
    #  currv = data[i][col]
    #  for j in range(i, len(data) - 1):
    #      nextv = data[j][col]
    #      if currv > nextv:
    #        data[i], data[j] = data[j], data[i]
    
    # 중복 인덱스 1번째 인덱스 기준 내림차순 정렬
    # col번째 인덱스 기준 오름차순 정렬
    #for i in range(0, len(data) - 1):
    #  currv = data[i][col-1]
    #  for j in range(i, len(data) - 1):
    #      nextv = data[j][col-1]
    #      if currv == nextv:
    #        if data[i][0] < data[j][0]:
    #        	data[i], data[j] = data[j], data[i]
    
    data = sorted(data, key = lambda x: [x[col - 1], -x[0]])
    
    # 나머지 합 계산 (S_i)
    totalSum = []
    for index in range(row_begin, row_end+1):
        sum = 0
        for v in data[index-1]:
            sum += v % index
        totalSum.append(sum)
    
    # 해시값 계산
    sum = 0
    for sum in totalSum:
        answer ^= sum
        
    return answer 

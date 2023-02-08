from collections import deque
def solution(priorities, location):
    dq = deque()
    
    # location index 문서 Mark
    for idx in range(len(priorities)):
        if idx == location:
            dq.append((priorities[idx], True))  # ex) 2, True (중요도, 찾는문서)
        else:
            dq.append((priorities[idx], False))
            
    # 대기열 시뮬레이션
    count = 0
    while len(dq) > 0:
        # 현재 문서 
        cur_doc = dq[0]

        # 큐 순회하며 현재 문서보다 큰 문서 확인
        max_doc = cur_doc
        max_doc_index = 0
        for j in range(len(dq)):
            if dq[j][0] > cur_doc[0]:
                max_doc = dq[j]
                max_doc_index = j
                break
                
        # 중요도가 높은 문서가 있는 경우 뒤로 보냄
        if max_doc[0] > cur_doc[0]:
            dq.append(cur_doc)
            dq.popleft()
            continue
        
        # 문서 처리       
        doc = dq.popleft()
        count+=1
        
        # 방금 처리한 문서가 원하는 문서였다면 끝
        if doc[1] == True:
            break
        
    return count 
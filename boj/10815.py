# binary search
def search(key, left, right):
    mid = (left + right) // 2
    
    # 종료 조건
    if cards[mid] == key:
        return True
    
    if left > right:
        return False
    
    if key > cards[mid]:
        return search(key, mid+1, right)
    elif key < cards[mid]:
        return search(key, left, mid-1)


n = int(input())
cards = sorted(list(map(int, input().split())))  # binary search를 위해 선 정렬
m = int(input())
checks = list(map(int, input().split()))
answers = []
for c in checks:
    if search(c, 0, n-1):
        answers.append('1 ')
    else:
        answers.append('0 ')
print(''.join(answers))

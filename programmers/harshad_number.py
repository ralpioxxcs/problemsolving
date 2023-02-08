def solution(x):
    answer = True
    nums = [x for x in (list(str(x)))]

    sum = 0
    for n in nums:
        sum += int(n)

    if x % sum == 0:
        return True
    else:
        return False
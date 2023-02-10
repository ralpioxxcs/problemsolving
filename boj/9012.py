def solve(input):
    stack = []
    for v in input:
        if v == "(":
            stack.append(v)
        # 반대편 괄호를 만난경우 현재 스택에서 pop하여 없앤다
        elif v == ")":
            # 처음부터 들어온경우 VPS 성립 X
            if len(stack) == 0:
                return "NO"
            stack.pop()
            
    # 비어있지 않으면 실패
    if len(stack) != 0:
        return "NO"
    
    return "YES"
    
for _ in range(int(input())):
    print(solve(list(input())))
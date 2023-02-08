def solution(s):
    answer = -1

    #while (len(s)):
    #    length = len(s)
    #    for idx in range(0, len(s)-1):
    #        if s[idx] == s[idx + 1]:
    #            s = s[:idx] + s[idx+2:]
    #            break
    #    if len(s) == length:
    #        break
    #if len(s) > 0:
    #    answer = 0
    #else:
    #    answer = 1

    words = []
    for w in s:
        if len(words) == 0:
            words.append(w)
            continue
        if words[-1] == w:
            words.pop()
        else:
            words.append(w)

    if len(words) > 0:
        answer = 0
    else:
        answer = 1

    return answer
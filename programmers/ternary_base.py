def solution(n):
    three = []
    while True:
        if n <=2:
            three.append(n)
            break
        three.append(n % 3)
        n = n//3

    three.reverse()
    print(three)
    seven = 0
    for index in range(len(three)):
        seven += three[index] * pow(3,index)
    return seven
a = int(input())
b = int(input())
aStr = list(map(str, str(a)))
bStr = list(map(str, str(b)))
print(a * int(bStr[2]))
print(a * int(bStr[1]))
print(a * int(bStr[0]))
print(a * b)
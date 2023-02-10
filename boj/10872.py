# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
fact = lambda n: 1 if n == 1 or n == 0 else n * fact(n-1)
print(fact(int(input())))
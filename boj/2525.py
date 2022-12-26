h,m = map(int,input().split())
tm = int(input())
print("{} {}".format((h + (tm // 60) + ((m + (tm % 60)) // 60)) % 24, (m + (tm % 60)) % 60))
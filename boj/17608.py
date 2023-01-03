import sys
heights = [int(sys.stdin.readline()) for x in range(int(sys.stdin.readline()))]
see = 0
long = heights[len(heights)-1]
while len(heights):
  h = heights.pop()
  if h > long:
    long = h
    see+=1
print(see+1)
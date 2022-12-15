import sys

students = {}
[students.setdefault(x+1, False) for x in range(30)]

present = []
for i in range(28):
    present.append(int(sys.stdin.readline()))

for i in range(len(present)):
    students[present[i]] = True

notpresent = []
for key in students:
    if students[key] == False:
        notpresent.append(key)

print(min(notpresent))
print(max(notpresent))

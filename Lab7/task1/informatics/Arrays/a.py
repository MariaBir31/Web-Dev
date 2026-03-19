
n = int(input())
a = []
line = input().split()
for x in line:
    a.append(int(x))

for i in range(0, n):
    if i % 2 == 0:
        print(a[i], end=" ")

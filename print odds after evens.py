a = list(map(int,input().split()))
n = int(input())
#a.sort()
#print(a[-2])
count = 0
for i in a[0:n]:
    if i % 2 == 0:
        count += 1
for i in a[0:n+1+count]:
    if i % 2 != 0:
        print(i)
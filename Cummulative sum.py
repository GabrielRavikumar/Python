l = list(map(int,input().split()))
cumulative_sum = []
total = 0
for i in l:
    if i >= 0:
        total += i
        cumulative_sum.append(total)
for i in cumulative_sum:
    print(i,end=" ")
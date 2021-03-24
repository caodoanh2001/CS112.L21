n = int(input())
a = list(map(int, input().split()))

p, q = 0, 0
i_less = 0
i_0 = -1
curr = -1
max_result = -9999999999

result = -9999999999
sum = 0

for i in range(0, n):
    if a[i] < 0 and a[i] > max_result:
        max_result = a[i]
        i_less = i
    if a[i] == 0 and i_0 < 0:
        i_0 = i
    sum += a[i]
    if sum < 0:
        curr = i
        sum = 0
    elif sum > result:
        p = curr
        q = i  
        result = sum
        
if result < 0:
    print(i_less + 1, i_less + 1, max_result)
elif result == 0:
    print(i_0 + 1, i_0 + 1, "0")
else:
    print(p + 2, q + 1, result)
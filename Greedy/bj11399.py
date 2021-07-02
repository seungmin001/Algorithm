n = int(input())
p_list = list(map(int, input().split()))
p_list.sort()

ans = 0
p_sum = 0
for p in p_list:
    p_sum += p
    ans += p_sum

print(ans)

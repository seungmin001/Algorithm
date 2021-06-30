ans = 0
N, M = map(int, input().split())
while N:
    temp_list = list(map(int, input().split()))
    # ans = max(ans,min(temp_list))
    temp_list.sort()
    if ans < temp_list[0]:
        ans = temp_list[0]
    N -= 1

print(ans)

ans=0
# 첫번째 줄 입력
N, M, K = input().split(' ')
N = int(N); M = int(M); K = int(K)
# 두번째 줄 입력
num_list = input().split()
for i in range(N):
    num_list[i] = int(num_list[i])

num_list.sort(reverse=True)

while M:
    for i in range(K):
        ans+=num_list[0]
        M-=1
        if not M:
            break
    if not M:
        break
    ans+=num_list[1]
    M-=1

print(ans)


## 예시
N, M, K = map(int, input().split(' '))  # first line
num_list = list(map(int, input().split()))  # second line
num_list.sort(reverse=True)

# 최댓값 K번+ 두번째큰값 1번 을 M회될때까지 반복
# 최댓값은 총 M // (K+1) * K + M % (K+1)번 더해짐
# 두번째큰값은 M - 최대값횟수

max_count = M // (K + 1) * K + M % (K + 1)
ans = num_list[0] * max_count
ans += num_list[1] * (M - max_count)
print(ans)

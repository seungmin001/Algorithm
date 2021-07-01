ans = 0  # N이 1일 될때까지의 최소 연산 횟수
N, K = map(int, input().split())

while N >= K:
    if N % K != 0:
        temp = N // K * K  # N에 가장 가까운 K의 배수
        ans += N - temp
        N = temp
    else:
        N = N // K
        ans += 1

ans += N - 1
print(ans)

# 다음을 N이 K보다 작아질 때까지 반복
# N이 K의 배수가 될 때 까지 1씩 빼기
# N을 K로 나누기
# 더이상 나눌 수 없으므로 남은 수만큼 1씩 빼기

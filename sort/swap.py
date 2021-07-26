# 두 배열의 원소 교체

# N(A,B의 원소 개수), K(바꿔치기 최대 횟수) 입력
n,k = map(int, input().split())

# A,B 입력
a =list(map(int,input().split()))
b =list(map(int,input().split()))

# A의 원소 합이 최대값이 되도록 해야한다.
# A는 오름차순, B를 내림차순으로 정렬하여 A의 원소가 더 커질때까지 혹은 K번까지 swap을 진행한다.
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i]>=b[i]:
        break
    a[i],b[i]=b[i],a[i]

print(sum(a))
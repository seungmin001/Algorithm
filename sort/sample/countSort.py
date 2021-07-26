# 계수 정렬 O(N+K) (> K는 최대값)
# 모든 원소가 0보다 크거나 같고, 최대값이 100만을 넘지 않을 때 사용

arr=[6,1,2,7,9]
# 배열 값의 범위를 포함할 만큼의 배열 생성
count = [0] * (max(arr)+1)

for i in range(len(arr)):
    count[arr[i]]+=1 # 각 데이터에 해당하는 인덱스의 값 증가

# 출현 횟수 확인
for i in range(len(count)): 
    # 오름차순으로 각 숫자의 등장 횟수 만큼 출력
    for j in range(count[i]):
        print(i, end=' ')
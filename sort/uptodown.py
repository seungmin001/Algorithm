# 위에서 아래로

n=int(input())
# n개의 데이터 입력
arr=[]
for i in range(n):
    arr.append(int(input()))
# 내림차순 정렬된 배열 출력
sortedArr=sorted(arr, reverse=True)
for i in sortedArr:
    print(i, end=' ')
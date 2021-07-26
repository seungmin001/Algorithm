# 퀵 소트 O(NlogN)
arr=[6,1,2,7,9]
arr1=[6,1,2,7,9]

# start, end, pivot 모두 index
def quick(arr,start,end):
    # 원소가 1개이면 끝
    if start >= end:
        return
    # hoare partition : 첫번째 원소를 pivot으로
    pivot=start
    left=start+1
    right=end
    
    while left <= right:
        # 더 큰 원소까지 진행
        while left <= end and arr[left] <= arr[pivot]:
            left+=1
        # 더 작은 원소까지 진행
        while right > start and arr[right] >= arr[pivot]:
            right-=1
        # 엇갈렸으면 pivot이랑 right(작은 원소)이랑 바꿈
        if left > right:
            arr[pivot], arr[right]= arr[right], arr[pivot]
        # 작은 원소, 큰 원소 swap
        else:
            arr[left], arr[right]= arr[right], arr[left]
    # pivot 기준 왼쪽, 오른쪽 분할 수행
    quick(arr,start,right-1)
    quick(arr,right+1,end)


def pyquick(arr):
    # 종료 조건
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    # pivot 제외 나머지
    tail=arr[1:]

    # pivot 보다 작거나 같은 애들
    left=[x for x in tail if x <= pivot]
    # pivot 보다 큰 애들
    right=[x for x in tail if x > pivot]

    return pyquick(left) + [pivot] + pyquick(right)

quick(arr,0,len(arr)-1)

print(arr)
print(pyquick(arr1))
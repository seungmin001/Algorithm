# 삽입 정렬 O

arr=[6,1,2,7,9]

def insertion(arr):
    for i in range(1,len(arr)):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            # 자기보다 작거나 같은 원소를 만날 경우 그 자리에 정착
            else:
                break

insertion(arr)
print(arr)
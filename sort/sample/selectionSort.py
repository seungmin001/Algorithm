# 선택 정렬 O(N^2)

arr=[6,1,2,7,9]

def selection(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index=j

        arr[i],arr[min_index] = arr[min_index], arr[i]

selection(arr)
print(arr)
# list는 이미 sort되어있는 것을 가정함
# 재귀 방식
def binarySearch(l, start, end, tgt):
    if start>end:
        return -1; # 찾을 수 없음
    
    mid = start + (end-start)//2

    if l[mid]>tgt: # target이 앞에 있음
        binarySearch(l,start,mid-1,tgt)
    elif l[mid]<tgt:
        binarySearch(l,mid+1,end,tgt)
    else:
        return mid

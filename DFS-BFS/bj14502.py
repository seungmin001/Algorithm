# 연구소
# 0: 빈칸 / 1: 벽 / 2:바이러스
from collections import deque
import copy
import sys
            
# input
input=sys.stdin.readline
n,m=map(int,input().split())
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

# 바이러스 위치 배열
virus=[]
for i in range(n):
    for j in range(m):
        if array[i][j]==2:
            virus.append((i,j))

# 벽 랜덤으로 세워보고 안전영역확인(최대값이면 교체)
max_safe=0


# 바이러스 퍼뜨리기
def bfs(array,a,b):
    # 상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    # queue 선언
    q=deque()
    q.append((a,b))
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if array[nx][ny]==0:
                    q.append((nx,ny))
                    array[nx][ny]=2
    

# 벽 3개 세우기
def wall_maker(cnt):
    global max_safe
    if cnt==3:
        cp_array=copy.deepcopy(array)
        for v1,v2 in virus:
            bfs(cp_array, v1,v2)
        # 2차원 배열에서 원하는 값 반복횟수 찾기
        safe=sum(i.count(0) for i in cp_array)
        max_safe=max(safe,max_safe)
    else:
        # 벽을 세우는 모든 방법 조회
        for i in range(n):
            for j in range(m):
                if array[i][j]==0:
                    array[i][j]=1
                    wall_maker(cnt+1)
                    array[i][j]=0

wall_maker(0)
#print(array)
print(max_safe)
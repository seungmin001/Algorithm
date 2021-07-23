# 3055 : 탈출
# . : 빈칸, S: Src, D: Dest, X: 돌, *: 물
from collections import deque
import sys

# input
input=sys.stdin.readline
r, c = map(int, input().split())
arr = []
visited = []
water = deque()

for i in range(r):
    arr.append(list(input().rstrip('\n')))
    visited.append([])
    for j in range(c):
        # source
        if arr[i][j] == 'S':
            src = (i, j)
        # water
        elif arr[i][j] == '*':
            water.append((i, j))
        # visited는 모두 0으로 초기화
        visited[i].append(0)

# 상하좌우 이동좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 물 이동 함수 (현재 water queue에 존재하는 좌표에 대해 빈칸으로 한 번 퍼지기)
def water_move():
    repeat = len(water)
    # 현재 저장된 water칸에 대해서만 실행
    for _ in range(repeat):
        x, y = water.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # array range check
            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                # 이동 가능 check
                if arr[nx][ny] == '.':
                    arr[nx][ny]='*'
                    # 다음 턴에 사용할 위치 queue에 추가
                    water.append((nx, ny))


# source to destination BFS
def escape():
    q = deque()
    q.append(src)
    
    # cur_minute이 증가할 때만 water_move하도록 변수 설정
    move_timing=0
    while q:
        # 고슴도치 현재 위치
        x, y = q.popleft()
        cur_minute=visited[x][y]
        arr[x][y]='S'

        # water move 먼저 이동. 
        if cur_minute == move_timing:
            water_move()
            move_timing+=1
        
        # 고슴도치 이동(BFS)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # array range check
            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                # dest 확인
                if arr[nx][ny]=='D':
                    print(cur_minute+1)
                    return
                # 이동 가능 check.
                if arr[nx][ny] == '.' and visited[nx][ny]==0:
                    # 다음에 이동할 곳 queue에 넣고 이동 시간 계산
                    visited[nx][ny] = cur_minute+1
                    q.append((nx,ny))         
    
    # 도착 못함
    print("KAKTUS")

escape()
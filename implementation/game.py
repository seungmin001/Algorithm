# 게임 개발 # 시뮬레이션
# 입력
n, m = map(int, input('').split())  # row, col size
x, y, direction = map(int, input('').split())  # 캐릭 위치, 방향
rows = []  # 맵 구조 0: 육지, 1: 바다
for i in range(n):
    rows.append(list(map(int, input('').split())))

# index 0: 북, 1: 동, 2: 남, 3: 서
move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

# 가본 칸 저장
store_loc = set([(x, y)])
ans = 1  # 캐릭터 방문 칸 수
dir_move = 0
while(1):
    # 갈 곳이 없을 경우
    if dir_move == 4:
        # 뒤로 갈 수 있는 지 확인(✔)
        next_x = x-move_x[direction]
        next_y = y-move_y[direction]
        if rows[next_x][next_y] == 0:
            x = next_x
            y = next_y
            dir_move = 0
            continue
        else:
            break

    # 1단계 반시계 90도 방향 변경
    if direction in [1, 2, 3]:
        direction -= 1
    elif direction == 0:
        direction = 3
    dir_move += 1

    # 2단계 현재 앞으로 갈 수 있는지 검사
    # 다음 위치
    next_x = x + move_x[direction]
    next_y = y + move_y[direction]

    # 못 가는 경우
    if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m or rows[next_x][next_y] == 1 or (next_x, next_y) in store_loc: # 외곽에 대한 설명을 잘못 이해해서 예외처리 함..
        continue
    else:  # 갈 수 있는 경우
        x = next_x
        y = next_y
        store_loc.add((x, y))
        ans += 1
        dir_move = 0

print(ans)




# 모범 답안
n, m = map(int, input('').split())  # row, col size

# 방문 위치 저장 -> 배열
d = [[0]*m for _ in range(n)] # 0으로 이루어진 길이 m의 배열(열)을 n개 가짐(행) # list comprehension

x, y, direction = map(int, input('').split())  # 캐릭 위치, 방향
d[x][y]=1 # 처음 위치

# 맵 정보
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

# 북, 동, 남 ,서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전 함수(방향 조절)
def turn_left():
    global direction
    direction -=1
    if direction==-1 :
        direction=3

# 시뮬레이션
count=1 # 답(방문한 칸 수)
turn_time=0
while True:
    # 1. 회전
    turn_left()
    nx= x+dx[direction]
    ny= y+dy[direction]
    # 2. 가보지 못한 칸 있으면 이동
    if d[nx][ny] ==0 and array[nx][ny]==0:
        x=nx
        y=ny
        d[nx][ny]=1
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    # 3. 못 가본 칸이 있다면
    if turn_time==4:  
        nx=x-dx[direction]
        ny=y-dy[direction]
        # 뒤로 갈 수 있다면
        if array[nx][ny]==0: 
            x=nx
            y=ny
        else:
            break
        turn_time=0

print(count)
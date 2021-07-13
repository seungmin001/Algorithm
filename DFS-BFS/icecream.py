# 음료수 얼려 먹기

# 2d array dfs
def dfs(graph, i, j):
    graph[i][j] = 1

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni >= 0 and ni < n and nj >= 0 and nj < m and not graph[ni][nj]:
            dfs(graph, ni, nj)

# input
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 1: 칸막이 0: 구멍
# 상하좌우 이동
di = [-1, 1, 0, 0]  # 행
dj = [0, 0, -1, 1]  # 열
ans = 0
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            ans += 1
            dfs(graph, i, j)

print(ans)


# 예시 답안
# dfs 들어간 후 방문여부 검사함
def dfs_ex(x,y):
    # out of Index일 시 바로 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 0 :
        # 노드 방문처리
        graph[x][y] = 1
        # 상하좌우 검사
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        # 연결되어있는 모든 노드를 방문했으므로 true반환
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs[n][m] == True:
            result+=1

print(result)
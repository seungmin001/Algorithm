# 미로 탈출
# (1,1) (N,M) 까지 가는 최소 이동 횟수
# 괴물 : 0 / 길 : 1
# BFS를 진행하며 모든 거리를 계산하여 저장한다.
from collections import deque

def main():
    # input
    n, m = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))


    def bfs(x, y):
        # 큐 생성
        queue = deque([(x, y)])

        # 상하좌우
        dx = [1, -1, 0, 0]  # 행
        dy = [0, 0, -1, 1]  # 열
        while queue:
            # 앞의 원소 pop
            x, y = queue.popleft()
            # 상하좌우 검사
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 접근 불가시 다음 검사
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                # 아직 방문하지 않은 곳 큐에 추가 및 거리 계산
                # 1의 거리가 변하는 것을 막으려면 nx ny != 0 을 추가하면 된다.
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

    bfs(0,0) # 1,1
    print(graph[n - 1][m - 1]) # n,m

if __name__== "__main__":
    main()
from collections import deque
import sys

def main():
    input=sys.stdin.readline
    # input
    n,m,start=map(int,input().split())

    # graph 설정
    graph=[[] for i in range(n+1)]
    # index 숫자 그대로로 쓰기 위해 n+1개 만듦
    
    # adjacent list 구성
    for _ in range(m):
        x,y=map(int,input().split())
        # 두 정점 사이 여러개의 간선 고려
        if y not in graph[x]:
            graph[x].append(y)
        if x not in graph[y]:
            graph[y].append(x)

    # 작은 순서로 가는 것 고려
    for i in graph:
        i.sort()

    # visited
    visited1=[False]*(n+1)
    visited2=[False]*(n+1)

    dfs(graph, start, visited1)
    print()
    bfs(graph, start, visited2)

def dfs(graph, v, visited):
    # 노드 방문처리
    visited[v]=True
    print(v, end=' ')
    # 인접한 노드 중 방문하지 않은 가장 작은 노드부터 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    # 큐 생성
    queue=deque()
    # 시작점 넣고 방문처리
    queue.append(start)
    visited[start]=True

    # 큐가 빌 때까지 반복
    while queue:
        # 가장 앞 노드 pop 및 출력
        node=queue.popleft()
        print(node, end=' ')
        # 인접한 노드 중 방문하지 않은 것 큐에 넣고 방문처리
        for i in graph[node]:
            if not visited[i]:                
                queue.append(i)
                visited[i]=True

if __name__=="__main__":
    main()
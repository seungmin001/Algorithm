def solution(board):
    answer = 0
    
    # lx , ly : board의 행 열 길이
    lx = len(board)
    ly = len(board[0])
    
    # 정사각형의 최대 변 길이
    ansroot=0
    # for문에서 접근 안하는 곳 확인
    if board[0][0] or board[1][0] or board[0][1]:
        ansroot=1
    
    # diagonal확인 가능한 1,1부터 확인
    for i in range(1,lx):
        for j in range(1,ly):
            if board[i][j]:
                # left, up, diagonal 위치 값 확인, 그 중 최소값 + 1으로 값 변경
                l = board[i][j-1]
                u = board[i-1][j] 
                d = board[i-1][j-1]
                minimum = min([l,u,d])
                board[i][j]= minimum+1
                # 최대 square 확인
                if minimum+1 > ansroot:
                    ansroot = minimum+1
                    
    answer = ansroot**2

    return answer
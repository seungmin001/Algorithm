# 참고 https://goodmilktea.tistory.com/56
for _ in range(3): # 3가지 case
    
    temp=[] # 전체 맵
    one_row=[] # row 기준
    one_col=[] # col 기준
    rcnt=-1 # 1이 있는 row개수
    ccnt=-1 # 1이 있는 col개수
    
    for i in range(6): # 한 줄당  6개 입력
        temp.append(list(map(int, input().split())))

    # row기준 모양 (col값 저장)
    for i in range(6):
        r_first=True
        for j in range(6):
            if temp[i][j] == 1:   
                if r_first:
                    one_row.append([])
                    rcnt+=1
                    r_first=False
                one_row[rcnt].append(j)
                
    # col기준 모양 (row값 저장)
    for j in range(6):
        c_first=True
        for i in range(6):
            if temp[i][j] == 1:
                if c_first:
                    one_col.append([])
                    ccnt+=1
                    c_first=False
                one_col[ccnt].append(i)

    # simulation 
    iscube=False
    # 가로로 긴 경우 > row 기준 비교
    if rcnt==2: # 3줄
        # 1 4 1
        if len(one_row[1])==4 and len(one_row[0])==1 and len(one_row[2])==1:
            iscube=True

        # 2 3 1 & 1 3 2 (2는 3의 끝 부분과 연결)
        if len(one_row[1])==3:
            if len(one_row[0])==2 and (one_row[0][1]==one_row[1][0] or one_row[0][0] == one_row[1][2]):
                iscube=True
            if len(one_row[2])==2 and (one_row[2][1]==one_row[1][0] or one_row[2][0] == one_row[1][2]):
                iscube=True
        
        # 2 2 2 (계단형)
        if len(one_row[0])==2 and len(one_row[1]) ==2 and len(one_row[2]) == 2:
            # 왼쪽형
            if one_row[0][1] == one_row[1][0] and one_row[1][1] == one_row[2][0]:
                iscube=True
            # 오른쪽형
            if one_row[0][0] == one_row[1][1] and one_row[1][0] == one_row[2][1]:
                iscube=True
        
    # 3 3
    if rcnt==1:
        if len(one_row[0])==3 and len(one_row[1])==3:
            # 왼쪽형
            if one_row[0][2]==one_row[1][0]:
                iscube=True
            # 오른쪽형
            if one_row[0][0]==one_row[1][2]:
                iscube=True

    # 세로로 긴 경우 > col 기준 비교 (row 비교 문을 모두 col으로 바꿔주면 된다)
    if ccnt==2: # 3줄
        # 1 4 1
        if len(one_col[1])==4 and len(one_col[0])==1 and len(one_col[2])==1:
            iscube=True

        # 2 3 1 & 1 3 2 (2는 3의 끝 부분과 연결)
        if len(one_col[1])==3:
            if len(one_col[0])==2 and (one_col[0][1]==one_col[1][0] or one_col[0][0] == one_col[1][2]):
                iscube=True
            if len(one_col[2])==2 and (one_col[2][1]==one_col[1][0] or one_col[2][0] == one_col[1][2]):
                iscube=True
        
        # 2 2 2 (계단형)
        if len(one_col[0])==2 and len(one_col[1]) ==2 and len(one_col[2]) == 2:
            # 왼쪽형
            if one_col[0][1] == one_col[1][0] and one_col[1][1] == one_col[2][0]:
                iscube=True
            # 오른쪽형
            if one_col[0][0] == one_col[1][1] and one_col[1][0] == one_col[2][1]:
                iscube=True
        
    # 3 3
    if ccnt==1:
        if len(one_col[0])==3 and len(one_col[1])==3:
            # 왼쪽형
            if one_col[0][2]==one_col[1][0]:
                iscube=True
            # 오른쪽형
            if one_col[0][0]==one_col[1][2]:
                iscube=True

    if iscube:
        print('yes')
    else:
        print('no')
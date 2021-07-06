# 왕실의 나이트
# 8 * 8 좌표 평면

rc = input('')
col = rc[0]  # 열
row = int(rc[1])  # 행

# valid col : a ~ h
# valid row : 1 ~ 8
ans = 0
# 1. row*2 col*1
temp = 0
if col != 'a':  # 왼
    temp += 1
if col != 'h':  # 오
    temp += 1

if row - 2 >= 1:  # 위
    ans += temp
if row + 2 <= 8:  # 아래
    ans += temp

# 2. col*2 row*1
temp = 0
if ord(col) - ord('a') >= 2:  # 왼
    temp += 1
if ord('h') - ord(col) >= 2:  # 오
    temp += 1

if row - 1 >= 1:
    ans += temp
if row + 1 <= 8:
    ans += temp

print(ans)


# 예시 답안
data = input()
row = int(data[1])
col = ord(data[0]) - ord('a')+1  # 알파벳에서 1~8사이 수로 변경

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2),
         (1, -2), (-1, 2), (1, 2)]  # 8가지 방향

ans = 0
for step in steps:
    next_row = row+step[0]
    next_col = col+step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        ans += 1

print(ans)

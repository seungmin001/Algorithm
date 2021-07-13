# 결혼식 5567
n =int(input()) # 동기 수 
m = int(input()) # 리스트 길이

# 친구 리스트 입력 받고 본인부터 검사하기 위해 작은번호 순 정렬
f_list=[]
for _ in range(m):
    x,y=map(int,input().split())
    f_list.append((x,y))
    f_list.append((y,x))
f_list.sort()

# 본인과 가까운 정도를 나타내는 인접 지수 계산
friend={1:0}
for a,b in f_list:
    # b가 key로 이미 있고, 인접 지수값이 a+1한 것보다 작을 때에는 pass
    if a in friend.keys():
        if b in friend.keys() and friend[b] < friend[a]+1:
            continue
        friend[b]=friend[a]+1

# 인접 지수 2 이하만 정답으로 인정
ans = -1 # 자기자신 제외
for f in friend:
    if friend[f] <=2:
        ans+=1

print(ans)

#f_list 튜플 넣을 때 작은,큰 큰,작은 두 경우 다 넣어야함 1,16 16,2의 경우 1,16 2,16 해서 2가 초대를 못받는 반례 존재
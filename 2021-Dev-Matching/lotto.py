# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = []
    same_set=set(lottos)&set(win_nums) # same_set 원소 개수 == 최저 당첨
    diff_l=[x for x in lottos if x ==0] # 0의 개수로 순위 결정
    low,high=len(same_set),len(same_set)+len(diff_l) # 최저, 최고 당첨 개수
    prize=[6,6,5,4,3,2,1] # index로 순위 설정
    
    answer.append(prize[high]) # 최고 순위
    answer.append(prize[low]) # 최저 순위
    return answer
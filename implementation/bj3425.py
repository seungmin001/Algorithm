# 고스택 풀이시간:2시간
import sys

def main():
    input = sys.stdin.readline

    while True:
        # 기계단위
        ins=[]
        num=[]

        while True:
            # 명령어 저장
            temp=input().split()

            if len(temp)==0: # 기계 사이 공백
                break
            elif temp[0]=="QUIT": # 더 이상 기계 없음
                return

            if temp[0]=="END": # 명령어 끝               
                n= int(input())
                for i in range(n):
                    num.append(int(input()))
                break # 저장해둔 명령어 실행
            ins.append(temp)

        # 저장해둔 명령어 차례로 실행
        for x in num:
            # 각 입력값에 대해 독립적으로 프로그램 수행
            stack=[x]
            result=0
            for i in ins:
                result=0 # 초기화
                if i[0]=="NUM":
                    result=push(stack,int(i[1]))
                elif i[0]=="POP":
                    result=pop(stack)
                elif i[0]=="INV":
                    result=inv(stack)
                elif i[0]=="DUP":
                    result=dup(stack)
                elif i[0]=="SWP":
                    result=swp(stack)
                elif i[0]=="ADD":
                    result=add(stack)
                elif i[0]=="SUB":
                    result=sub(stack)
                elif i[0]=="MUL":
                    result=mul(stack)
                elif i[0]=="DIV":
                    result=div(stack)
                elif i[0]=="MOD":
                    result=mod(stack)
                
                # 에러가 발생했을 때는 다음 명령을 수행하지 않고 종료한다.
                if result==-1:
                    break
            
            if len(stack)!=1 or result==-1: # 수행 종료 후 스택에는 하나의 원소만 있어야함. error중복 출력 방지
                print("ERROR")
                continue
            print(stack[0])

        # 빈 줄 / 기계사이 공백만 받았을 때 공백 출력 x
        if len(num)>0:
            print()

# return 0 # ok
# return -1 # error 상황        
def push(stk, n):
    stk.append(n)
    return 0 # push은 에러 상황 없음

def pop(stk):
    if len(stk)<1: # pop할 수 없음
        return -1
    stk.pop()
    return 0

def inv(stk):
    if len(stk)<1: # 맨 위 원소가 없음
        return -1
    x=stk.pop()
    x=(-1)*x # 반전
    stk.append(x)
    return 0

def dup(stk):
    if len(stk)<1: # 맨 위 원소가 없음
        return -1
    stk.append(stk[len(stk)-1])
    return 0

def swp(stk):
    if len(stk)<2: # 2개 원소가 없음
        return -1
    stk[len(stk)-1], stk[len(stk)-2] = stk[len(stk)-2], stk[len(stk)-1]
    return 0

def add(stk):
    if len(stk)<2: # 2개 원소가 없음
        return -1
    x=stk.pop()
    y=stk.pop()
    if abs(x+y) > 1_000_000_000: # 절댓값이 10^9를 넘을 수 없음
        return -1
    stk.append(x+y)
    return 0

def sub(stk):
    if len(stk)<2: # 2개 원소가 없음
        return -1
    x=stk.pop()
    y=stk.pop()
    if abs(y-x) > 1_000_000_000: # 두번째-첫번째 절댓값이 10^9를 넘을 수 없음
        return -1
    stk.append(y-x)
    return 0

def mul(stk):
    if len(stk)<2: # 2개 원소가 없음
        return -1
    x=stk.pop()
    y=stk.pop()
    if abs(x*y) > 1_000_000_000: # 두번째-첫번째 절댓값이 10^9를 넘을 수 없음
        return -1
    stk.append(x*y)
    return 0

def div(stk):
    if len(stk)<2: # 2개 원소가 없음
        return -1
    x=stk.pop()
    y=stk.pop()
    # 계산은 절댓값으로
    # 피연산자 중 음수가 한 개 일때만 몫의 부호가 음수.    
    sign=0
    if y<0:
        y=(-1)*y # 반전
        sign+=1
    if x<0:
        x=(-1)*x # 반전
        sign+=1
    # 0으로 나누는 경우 처리
    if x==0:
        return -1
    r=int(y/x)
    if sign%2 ==1:
        r=(-1)*r
    stk.append(r)
    return 0

def mod(stk):
    if len(stk)<2: # 2개 원소가 없음
        return -1
    x=stk.pop()
    y=stk.pop()
    # 계산은 절댓값으로
    # 피제수가 음수이면 나머지도 음수
    sign=0
    if y<0:
        y=(-1)*y # 반전
        sign+=1
    if x<0:
        x=(-1)*x # 반전
        
    # 0으로 나누는 경우 처리
    if x==0:
        return -1
    r=y%x
    if sign ==1:
        r=(-1)*r
    stk.append(r)
    return 0

if __name__=="__main__":
    main()
# 성적이 낮은 순으로 학생 이름 출력하기

n = int(input())
d = {}
for i in range(n):
    name, grade= input().split()
    grade=int(grade)
    d[name]=grade

sorted_dict=sorted(d, key=lambda student:d[student]) # student에 dict의 key값이 넘어옴
for i in sorted_dict:
    print(i, end=' ')

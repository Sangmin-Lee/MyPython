#b = [1,2,3]
#c = ['Life', 'is', 'too', 'short']

#print(b+c)      #strcat
#f = b+c
#print(f)
#f[3] = 'greenjoa'
#print(f[3:4])   #List
##[3:4] == (3<= x < 4)
#print(f[3])     #Variable
#print(b*3)      #반복
#f.insert(3,'e') #insert
#f.append('asdf')#마지막에 추가
#f.remove('asdf')#직접 쓴 것과 비교해서 삭제
#f[1:2] = []     #빈칸으로 만들어 삭제
#print(f)
#del f[0]    #인자값으로 삭제
#print(f)
#print(f.index('greenjoa')) #이 데이터가 없으면 에러 발생

id = ['sangmin', 'boha']    #아이디 옆에 패스워드 추가하기
id.insert(id.index('sangmin')+1, 'tkdals')
print(id)
id.insert(2+1, 'qhgk')
print(id)

sub = ['dltkdals', '01051305773']   #패스워드 옆에 추가정보 넣기
id.insert(id.index('tkdals')+1, sub)
print(id)

nId = len(id)
print(range(nId))
for steps in range(nId) :   # 들여쓰기로 for문 구분 맨 끝에는 :(콜론) 
    print(id[steps])        # range 함수도 list 생성
for steps in id :
    print(steps)

scores = [85, 62, 37, 83, 10, 29]
scores.sort()   #오름차순
print(scores)
scores.reverse()#그냥 뒤집기
print(scores)

top5 = []   #정렬해서 큰 순서대로 5개 출력
for steps in range(5) :
    top5.insert(steps, scores[steps])
print(top5)

for steps in id :           # 리스트 안에 리스트가 있으면 각각 출력
    if isinstance(steps, list) :    #isinstance(변수, 자료형)
        for steps2 in steps :
            print(steps2)
    else :
        print(steps)

scores.pop()
scores.pop(3)
print(scores.count(62))
scores.extend([50, 60]) # 그냥 붙이기
print(scores)
scores.append([50, 60]) # 리스트로 붙이기
print(scores)

t1 = ()
t2 = (1,) # t2 = (1)과 다름
t6 = (1)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a', 'b', ('ab', 'cd'))

print(t1)
print(t2)
print(t6)
print(t3)
print(t4)
print(t5)
print(t5[0])
print(t5[1:])
print(t2+t3)
print(t4*3)
# 변경 연산 시 에러 발생
dic1 = {}
dic2 = dict()
dic = {'name':'pey', 'phone':'01051035773'}
print(dic['name'])      #pey
dic['birth'] = '1212'
print(dic)              #랜덤출력
del dic['name']
print(dic.keys())       #key값
print(dic.values())     #value값

b = list(dic.keys())    #리스트로 반환
print(b)

b = dic.items()         #튜플로써 묶여진 형태의 값을 반환
print(b)

#dic.clear()            #지우기
print(dic.get('name'))  #None
print(dic.get('birth')) #1212
dic.get('name','sm')    #해당 key가 없으면 default로 sm
'name' in dic           #key가 있는지 조사

#영화 별점주기 실습
#dic 안에 dic
movies = {'홍길동':{'베테랑':5.0,'암살':4.5},'고길동':{'베테랑':3.5,'암살':3.0}}
print(movies['홍길동'])         #홍길동이 준 점수들
#print(movies.get('홍길동'))
print(movies['홍길동']['암살'])  #암살 점수만
#print(movies.get('홍길동').get('암살'))

#대소문자 구분
# == != < > <= >= and or not 조건문에 응용
answer = input("Would you like express shipping? : ")
answer = answer.lower()
if answer == "yes" :
    print("That will be an extra $10")

pocket = ['paper', 'money', 'cellphone']
if 'card' in pocket: pass   # pass 사용법. 한 줄일 때 사용법
else: print("카드를 꺼내라")

a = [(1,2), (3,4), (5,6)]
for (first, last) in a :    #a의 튜플 하나씩 가져오는데 first, last로 이름을 붙이고
    print(first + last)     #first+last 해서 출력

for steps in range(1,10,2) :
    print(steps)            #1,3,5,7,9

#구구단 출력
#print하면 기본적으로 줄바꿈이 되는데 end=" " 옵션을 주면
#줄바꿈 하지않고 " " 공백 한 칸 출력
for i in range(2,10):
    for j in range(1,10):
        print('{0:d}*{1:d}={2:d}'.format(i,j,i*j), end=" ")
    print('')

#turtle 라이브러리 불러오기
import turtle
#for steps in range(4):  #4번 움직여라
#    turtle.forward(100)
#    turtle.right(90)

nSides = 7  # 7각형 안에 7각형
for steps in ['red','blue','green','black','yellow','cyan','purple']:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(360/nSides)
    for moresteps in range(nSides):
        turtle.forward(50)
        turtle.right(360/nSides)
input("")

#여러 줄에 걸쳐있는 것을 하나의 문자열로 선언
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    print(prompt, end="")
    number = int(input())
# 반복문 나갈 때 break / 조건으로 분기하고 싶으면 continue

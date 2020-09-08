#*변수*
#1 : 변수들의 평균출력
국어=50
수학=80
영어=30
print ("평균=")
print (((국어+수학+영어)//3))
#값 앞에 '평균='을 포항시키고 싶은데 자구 에러가 나요

#2 :  홀짝 판별 : 이프문
num = 409298570
if num%2==0 :
    print("짝수")
else :
    print("홀수")

#3 : 문자열의 출력
a= "국어:수학:영어:프로그래밍"
print (a[0:2],a[3:5],a[6:8],a[9:14])
print(a[:])
#반점을 어떻게 찍는거죠,,, 왜 오류만 날까요,,

#4 : 리스트 속 순서 바꾸기
b=[1, 70, 3, 80, 5]
print(b[4],b[3],b[2],b[1],b[0])
#이렇게 하는건지는 모르겠지만 일단 할 수 있는 만큼 한 결과입니다..ㅎ

#5 : 리스트 요소 배열 
c=["파이썬은", "정말", "편하다"]
print(c[0],c[1],c[2])

#6 : 리스트 요소 오름차순 정렬 : sort()사용
d= [1, 50, 410, 10, 3, 4, 5]
d.sort()
print (d)

#7 : 공백지우기 : strip()사
e=" I love python "
e.strip()
print(e)

#*제어문*
#1 : 1-100 더하기 :  포문사용
f=0
for g in range(1,101):
    f = f+g
print(f)

#2 : 1-100더하기 : 와일문 사용
h=1
sum=0
while h<101:
    sum=sum+h
    h=h+1
print(sum)

#3 : 1-100사이의 3의배수들의 합, 왜인지 3/9/이런식으로만 나온다..
'''i=1
sum=0
while i<101 :
    if i%3==0:
        sum=sum+i
        i=i+1
print(sum)'''
#포문도 써보고 와일도 써보고 순서도 바꿔봤는데 왜 안되는지 모르겠습니다..따흐흑..

#4 : 리스트 속 요소들의 평균구하기 : sum 만들기
A=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
for num in A:
    sum=sum+num
print(sum//10)
'''avg=sum/len(A)
print(avg) 라고 해도됨'''

#5 : 리스트 속 홀슈인 요소에 2를 곱한 후 배열 보여주기(배열 요서 변경)
B= [1, 3, 5, 40, 90, 100, 2020]
for b in B:
    if b%2==1:
        B[b]=b*2
print(B)
#조건을 충족한 특정 요소의 값만 2를 곱하는 방법을 모르겠습니다.

#6 : 별 찍기 : 포문
for n in range(1,6):
    print('*'*n)
print()

# *함수와 입출력*
#1 : 성적계산기 : 입력과 이프문
G=int(input('성적을 입력하세요 :'))
if 79<G<101:
    print("A")
elif 49<G<80:
    print('B')
elif 29<G<50:
    print('C')
else:
    print('F')


#2 : 숫자 입력후 짝,홀수 판별
o=int(input('숫자를 입력하세요 :'))
if o%2==0:
    print("True")
else:
    print("False")

#3 : 주민번호로 태어난 해와 성별 맞추기 : 문자열 슬라이싱과 조건문
K=input('주민등록번호를 입력하세요 :')

birth = K[0:2]
gender = K[7]

if (gender=='2' or gender=='4'): #gender를 숫자가 아닌 문자로 받아서 gender%2==0으로 못함.
    gender="여자"
else :
    gender="남자"
print(birth,"년생, ", gender)

#4 : 사칙연산, 0으로 나누면 안됨
'''
def add():
    a=int(input)
    b=int(input)
    result = a+b
    print(result)

def min():
    a=int(input)
    b=int(input)
    result = a-b
    print(result)

def mul():
    a=int(input)
    b=int(input)
    result = a*b
    print(result)

def div():
    a=int(input)
    b=int(input)
    result = a//b
    if b==0:
        print("수식이 잘못되었습니다.")
    print(result)
    

def re():
    a=int(input)
    b=int(input)
    result = a%b
    print(result)
    '''
#제가 한게 맞는 건지 모르겠습니다,, 이상한것 같긴 한데,, 파이썬으로 돌릴때 애초에 계산이 됩니다,,,ㅠㅠ

#5 : 거스름돈 함수 : 나누기 몫을 이용한 지폐선택
'''
def Q(pay,cost):
    q = pay-cost
    a = int(q/50000)
    print("50000원 지폐",a,"장")
    q = q%50000 #오만원을 나누고 난 나머지를 가지고 담은 지폐 수 결정
    
    b = int(q/10000)
    print("10000원 지폐",b,"장")
    q=q%10000
    
    c=int(q/5000)
    print("5000원 지폐",c,"장")
    q=q%5000
    
    d=int(q/1000)
    print("1000원 지폐",d,"장")
    q=q%1000
    
    e=int(q/500)
    print("500원 동전",e,"개")
    q=q%500
    
    f=int(q/100)
    print("100원 동전",f,"개")
    q=q%100
    
    g=int(q/50)
    print("50원 동전",g,"개")
    q=q%50
    
    h=int(q/10)
    print("10원 동전",h,"개")
    q=q%10
'''
#찾아보니 %d원 지폐, %d장 이러던데 %d가 뭔가요??
#왜 입력창이 뜨지 않을까요..?

#6 : 이차방정식의 근 구하기
#허근일 경우 ? 근의공식 ? 완전제곱식?
#...도대체 매쓰 라이브러리가 어디있죠...?













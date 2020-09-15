'''2주차 과제'''
#함수응용(예외처리 필수)

#1. 로또 번호 생성기 함수 만들기, 정렬까지 포함할 것.
try:
    num1=int(input())
    num2=int(input())
    num3=int(input())
    num4=int(input())
    num5=int(input())
    num6=int(input())
    print(num1,num2,num3,num4,num5,num6)

except IndexError as e:
    print("1~45사이의 정수만 입력 가능합니다.")
finally:
    print("try문 끝!")
    
'''1~45까지의 정수가 아닐 경우 오류 발생, 숫자 중복시 오류 발생, 자연수가 아닐시에 오류 발생
을 만들고 싶은데 어떤 예외의 종류를 사용해야 할지 모르겠습니다,,'''




#2. 다음과 같은 계산기 코드가 있을 때, 상세하게 살을 덧붙이고, 예외처리와 모듈화를 진행하라.

try:
    import example2
   
except ZeroDivisionError as e:
    print("0으로 나누면 안돼요~")

#3. 다음과 같이 문자열을 분석하는 함수를 만들어라. 내장함수를 이용하라|len,max,
#input : python , output : 문자의 개수 : 6, 가장 큰 문자열 : y, 뒤집은 문자열 : nohtyp
A=input('문자를 입력하세요.')
print(len(A))
print(max(A))
#뒤집은 문자열의 내장함수를 찾지 못했습니다,,

#4. 내장함수와 datetime라이브러리를 이용하여 지금을 출력하고, 49일 1시간 8분 7초 후가 언제인지 출력하는 함수를 만드시오.
import datetime
now = datetime.datetime.now()
print (now)

delta = datetime.timedelta(days=49, hours=1, minutes=8, seconds=7)
diff = now + delta

print("현 시간 부터 49일 1시간 8분 7초 후")
print(diff)

#5. 영한사전 프로그램을 만들어라. 딕셔너리를 이용할 것, 모듈화/예외처리 할 것
'''
K=input()
try
except
죄송합니다 모르겠습니다...ㅠ
'''

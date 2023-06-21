# 자료의 타입형 파악
a = True
type(a)     # <class 'bool'>



# 복사
a = [1, 2, 3]
b = a
id(a)   
id(b)   # 위의 id(a)와 id(b)는 결과값이 같다. 즉, 메모리 주소가 같다는 뜻
a is b  # True   따라서 이 경우, a를 수정하면 b도 수정이 되어버린다

# [:] 를 이용한 복사
a = [1, 2, 3]
b = a[:]    # : 앞뒤로 숫자가 없으니, a 리스트 전체를 의미

# copy 를 이용한 복사
from copy import copy   # 파이썬 모듈
a = [1, 2, 3]
b = copy(a)         # b = a[:] 와 동일
b is a              # False



# 제어문
# if문
if True:
    print("True")
elif 2 >= 1:
    print("hello")
else:
    print("False")

# 조건부 표현식
score = 70
if score >= 60:
    message = "success"  # pass 를 쓰면 아무 작업도 하지 않고 넘기기 가능
else:
    message = "failure"
# 을 다음과 같이 표현 가능
message = "success" if score >= 60 else "failure"

# while문
while True:
    print("hehe")
    break       # while문을 탈출
    continue    # while문의 맨 처음 조건문으로 복귀

# for문
# range로 횟수를 지정
for i in range(0, 10):
    break

# 리스트로 횟수 및 값을 지정 / 리스트, 튜플, 문자열 다 가능
test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

# 튜플의 for문 대입
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

# 구구단
for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ")     # end는 줄바꿈을 하지 않기 위함, 또한 숫자 사이에 간격을 위함
    print('') 
# 아래와 같이 표현도 가능
result = [x*y for x in range(2,10) for y in range(1,10)]



# 함수
def add(a, b):
    return a+b

# 입력값을 여러개 받아야 하는 경우
def add(*args):
    return 0

# 키워드 매개변수
# 매개변수 앞에 ** 를 붙이면, 매개변수는 딕셔너리가 되어 값이 딕셔너리에 저장이 됨
# kwargs 는 keyword arguments의 약자
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)   # {'a': 1}
print_kwargs(name='foo', age=3)     # {'age': 3, 'name': 'foo'}

# 리턴 값은 언제나 하나
def add_and_mul(a,b): 
    return a+b, a*b
# 위와 같이 리턴을 할 경우, 어느 하나 혹은 앞에 있는 a+b를 리턴 하는 것이 아닌,
# (a+b, a*b) 와 같은 튜플로 리턴을 하게 된다
result = add_and_mul(3,4)   # result = (7, 12)
# 각각 리턴을 받고 싶을 경우, 변수를 두 개를 선언하면 된다
result1, result2 = add_and_mul(3, 4)    # result1 = 7, result2 = 12

# 매개변수 선 설정
# 초기화를 미리 해놓고 싶은 매개변수는 항상 가장 마지막에 존재해야만 함
def say_myself(name, old, man=True):
    return
# 호출에는 두 가지 방법이 존재
say_myself("홍길동", 3)
say_myself("홍길동", 5, True)

# 외부의 변수와 함수 내부의 변수는 서로 다른 변수로 취급을 받음
# 설령 def 에서 a를 변수로 받고, 밖에 a라는 변수가 존재해도 이 두 a는 서로 다른 변수
# 함수 내부에서 수정한 a의 값을 밖의 a에 적용하고 싶을 경우, return 받은 값을 a에 대입을 하거나,
# 아래와 같이 global 명령어를 사용 가능
a = 1 
def vartest(): 
    global a 
    a = a+1
vartest()

# 람다식
add = lambda a, b: a+b
result = add(3, 4)
result  # 7



# 사용자에게 입력값 받기
a = input()



# 파일 생성
f = open("새 파일.txt", 'w')    # r : 읽기 모드, w : 쓰기 모드(기존 파일의 내용을 다 밀어버리고 새로 작성), a : 추가 모드(파일의 마지막에 새로운 내용 추가)
f.close         # 파이썬은 프로그램이 종료될 시 자동으로 닫히나, 명시적으로 작성해주는게 좋음

# 파일 위치 지정
f = open("C:/doit/새파일.txt", 'w')

# 파일 쓰기
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 파일 읽기
# 첫 줄만 출력
f = open("C:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

# 파일의 모든 줄 출력
# 마지막 줄의 다음이 되면 읽을 것이 더이상 없어 False가 되기에 자동으로 루프 종료
f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
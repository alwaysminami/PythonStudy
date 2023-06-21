# 파이썬은 자바와 같은 중괄호의 구분이 없고, 들여쓰기를 원칙으로 함
# 변수 선언 시 명시적인 변수의 형 선언이 필요하지 않음

# 이렇게 선언 시 int형으로,
a = 1

# 이렇게 선언 시 string으로 되는 식 
a = 'str'

# int, string 뿐만 아니라, List, float, double 등등 형에 다 적용되는 이야기.
# 다만, 자바와 같은 int + string 혹은 string + int 같은 사용은 불가능함

# " 와 ' 는 동일하게 작용
a = "wow"
a = 'wow'



# 문자열
a = "Life is too short, You need Python"
a[1]    # i
a[-2]   # o / -1이 마지막, -1부터 1씩 감소하며 앞으로
a[0:2]  # 'Li' / 슬라이싱

# 포매팅 / %s 는 string, %d 는 integer, %c는 char 등
"%f" % 3.42134234



# 리스트
# 대괄호 []로 감싸고, , 로 원소를 구분
list = [1, 3, 5, 7, 9]

# 다음과 같이 복합적으로 선언도 가능
a = [1, 2, 'Life', 'is']
b = [1, 2, ['Life', 'is']]

# 빈 리스트의 선언 방법은 두 가지
c = []
c = list()

# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
a[0:2]      # [1, 2]
b = a[:2]   # [1, 2]
c = a[2:]   # [3, 4, 5]

# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
a + b   # [1, 2, 3, 4, 5, 6]
a * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
len(a)  # 3

# 리스트 수정 및 삭제
a = [1, 2, 3]
a[2] = 4
a           # [1, 2, 4]
del a[1]
a           # [1, 3]
del a[2:]   # 와 같이 여러 개 동시 삭제도 가능. a.remove[n] 도 있음

# 리스트 요소 추가
a = [1, 2, 3]
a.append(4) # a.append([1, 2]) 같이 리스트 등등 어떠한 자료형도 추가 가능
a           # [1, 2, 3, 4]

# sort(), reverse(), index(), insert(a, b), count(n), a.extend(b) = a += b(리스트끼리 합치기. 리스트 확장)



# 튜플
# 리스트는 [], 튜플은 ()
# 리스트는 원소의 생성, 삭제, 수정이 가능. 튜플은 불가능
t1 = ()         # 빈 튜플
t2 = (1,)       # 원소가 하나 뿐일 경우, 원소 뒤에 , 가 필요함
t3 = (1, 2, 3)
t4 = 1, 2, 3    # 소괄호 생략 가능
t5 = ('a', 'b', ('ab', 'cd'))



# 딕셔너리
# Key와 Value를 가지는 자료형. 자바의 Map과 비슷함. 딕셔너리 혹은 해시라고도 칭함
# {Key1: Value1, Key2: Value2, Key3: Value3, ...} 와 같은 형태를 지님
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

# 딕셔너리 쌍 추가, 삭제
a = {1: 'a'}
a[2] = 'b'
a   # {1: 'a', 2: 'b'}
a['name'] = 'pey'
a   # {1: 'a', 2: 'b', 'name': 'pey'}
del a[1]    # 키 값을 기준으로 삭제
a   # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리에서 Key를 사용하여 Value 얻기
grade = {'pey': 10, 'julliet': 99}
grade['pey']      # 10
grade['julliet']  # 99
grade.get('pey')  # 10
grade.get('julliet') # 99

# Key 리스트 만들기
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.keys()    # dict_keys(['name', 'phone', 'birth']) 
a.values()  # dict_values(['pey', '010-9999-1234', '1118'])

# Key 값을 이용하여 반복문
for k in a.keys():
    print(k)

# Key, Value 쌍 얻기
a.items()   # dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')]) 

# Key, Value 쌍 모두 지우기
a.clear

# Key 값 유무 조사
'xxx' in a  # return 값은 true or false



# 집합 자료형
# 집합 자료형은 중복을 허용하지 않으며, 중복을 허용하지 않는 특성으로 인해, 필터로 사용되기도 함
# 집합 자료형은 순서가 없기 때문에, s1[0] 같은 인덱싱이 불가능
s1 = set([1, 2, 3,])
s1  # {1, 2, 3}
s2 = set("Hello")
s2  # {'l', 'o', 'H', 'e'}
s3 = set()

# 집합 자료형의 인덱싱 과정
s1 = set([1, 2, 3])
l1 = list(s1)
l1      # [1, 2, 3]
l1[0]   # 1
t1 = tuple(s1)
t1      # (1, 2, 3)
t1[0]   # 1

# 교집합, 합집합, 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s1 & s2     # {4, 5, 6}   & 혹은 s1.intersection(s2)
s1 | s2     # {1, 2, 3, 4, 5, 6, 7, 8, 9}   | 혹은 s1.union(s2)
s1 - s2     # {1, 2, 3}   - 혹은 s1.difference(s2)
s2 - s1     # {7, 8, 9}   

# 값의 추가, 제거
s1 = set([1, 2, 3])
s1.add(4)
s1      # {1, 2, 3, 4}
s1.update([5, 6])
s1      # {1, 2, 3, 4, 5, 6}
s1.remove(3)
s1      # {1, 2, 4, 5, 6}
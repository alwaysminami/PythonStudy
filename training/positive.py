# filter(함수, 반복 가능한 데이터)
# filter 은 첫 번째 인수로 함수, 두 번째 인수로 그 함수에 들어갈 반복 가능한 데이터를 받음
# 반복 가능한 데이터 중 리턴값이 True인 것만 묶어서 리턴

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result
    
print(positive([1,-3,2,0,-5,6]))


# 위와 같은 함수를 filter을 사용하여 아래와 같이 변경 가능

def positive1(x):
    return x > 0

print(list(filter(positive1, [1, -3, 2, 0, -5, 6])))
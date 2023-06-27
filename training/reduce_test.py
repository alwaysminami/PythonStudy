import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)

# 아래의 코드를 압축한 것
#
# def add(data):
#     result = 0
#     for i in data:
#         result += i
#     return result

# data = [1, 2, 3, 4, 5]
# result = add(data)
# print(result)
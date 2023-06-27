from operator import itemgetter

students_tuple = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

students_dic = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]

# 1번인 나이를 key로 전달, students_tuple의 튜플을 sort
result = sorted(students_tuple, key=itemgetter(1))
print(result)

# 딕셔너리의 키값인 age를 key로 전달, students_dic인 딕셔너리를 sort
result = sorted(students_dic, key=itemgetter('age'))
print(result)
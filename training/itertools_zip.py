import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']

# result = zip(students, snacks)
# print(list(result))

result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))
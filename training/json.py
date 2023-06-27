# 아래와 같은 ~~.json 파일이 있다면,
# {
#     "name": "홍길동",
#     "birth": "0525",
#     "age": 30
# }

import json

# json 파일을 읽어와 딕셔너리로 변환 / json.load(파일_객체)
with open('myinfo.json') as f:
    data = json.load(f)

type(data)  # <class 'dict'>
data        # {'name': '홍길동', 'birth': '0525', 'age': 30}


# 딕셔너리를 json으로 변환 / json.dump(딕셔너리, 파일_객체)
data = {'name': '홍길동', 'birth': '0525', 'age': 30}

with open('myinfo.json', 'w') as f:
    json.dump(data, f)


# 파이썬 자료형을 json 문자열로 변환
# 딕셔너리 -> json의 경우 데이터를 아스키 형태로 저장하기에 한글이 아래와 같이 표현됨
d = {"name":"홍길동", "birth":"0525", "age": 30}
json_data = json.dumps(d)
json_data   # '{"name": "\\ud64d\\uae38\\ub3d9", "birth": "0525", "age": 30}'

# 위의 json 문자열을 딕셔너리로 역변환하여 사용하는 것에 글자는 문제가 ㅇ벗음
json.loads(json_data)   # {'name': '홍길동', 'birth': '0525', 'age': 30}

# 위와 같이 아스키 형태로 변환하지 않으려면, ensure_ascii=False를 추가하면 변환되지 않음
json_data = json.dumps(d, ensure_ascii=False)
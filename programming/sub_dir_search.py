import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search("c:/")


# os.walk는 시작 디렉토리부터 하위에 있는 모든 디렉토리를 차례로 방문하는 함수
# 따라서 위의 함수를 더 간단하게 아래와 같이 작성 가능
# for(path, dir, files) in os.walk("c:/"):
#     for filename in files:
#         ext = os.path.splitext(filename)[-1]
#         if ext == '.py':
#             print("%s/%s" % (path, filename))
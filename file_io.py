def process(filename):
    with open(filename, "r", encoding='UTF-8') as f:
        # 키 : 알파벳, 값 : 빈도수
        dict = {}
        data = f.read()
        for i in data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict
dict = process("input.txt")
# 빈도수를 기준으로 내림차순 정렬을 수행한다
dict = sorted(dict.items(), key=lambda a:a[1], reverse=True)
for data, count in dict:
    if data == '\n' or data == ' ':
        continue
    print("%d번 출현: [%c]" %(count, data))
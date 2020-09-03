# 사전(Dictionary): 키(Key)와 값(Value) 한 쌍을 원소로 가지는 자료형
dict = {}
dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'effort'
dict['안녕'] = 'Hi'
print("사전 자료형의 길이", len(dict))
keys = dict.keys()
key_list = list(keys)
print("키 리스트: ", key_list)
values = dict.values()
value_list = list(values)
print("Value List: ", value_list)

if '노력' in dict:
    print("노력 키가 존재합니다")


del dict['기적']
dict.clear()
print("사전 자료형의 길이", len(dict))
for i, k in enumerate(dict):
    print("[인덱스: ", i, "] 한글: ", k, "/ 영어: ", dict[k])

scores = {}
scores['나동빈'] = 78
scores['이태일'] = 99
scores['박한울'] = 85
print(sorted(scores))       # 키 정렬하기 (기본 오름차순)
print(sorted(scores, reverse = True))   # 키 내림차순 정렬하기
print(sorted(scores.values()))      # 값 정렬하기
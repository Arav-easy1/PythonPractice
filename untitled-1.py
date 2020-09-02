# -*- Encoding: utf-8 -*-
# 리스트: 비슷한 성질을 가진 객체의 나열
# 인덱스: 0    1    2    3    4    5
# 값 :   3.5 4.3  2.3   3.8  3.2  4.5
#a = [3.5, 4.3, 2.4, 4.8, 3.2, 4.5]
#print("인덱스 0 = ", a[0])
#sum = 0
#for i in a:
    #sum = sum + i
#print("평균 점수: ", sum / len(a))

a = [
    [90, 95, 35, 95, 37, 65, 4, 54, 76, 100],
    [12, 23, 34, 54, 67, 89, 76, 54, 65, 76]
]
sum = 0
english = a[0]
for i in english:
    sum = sum + i
print("영어 평균 점수: ", sum / len(english))
sum = 0
math = a[1]
for i in math:
    sum = sum + i
print("수학 평균 점수: ", sum / len(math))
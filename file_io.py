# open(): 파일을 특정한 모드로 여는 함수입니다. 읽을 때는 r, 쓸 때는 w
# read(): 파일 객체로부터 모든 내용을 읽는 함수입니다.
f = open("input.txt", "r", encoding="UTF-8")
f.seek(3)   # 9바이트의 위치부터 파일을 읽겠다. 한글은 3바이트씩 차지한다(일반적, 다를 수 있음)
data = f.read()
print(data)
f.close()

# readline(): 파일 객체로부터 한 줄 씩 문자열을 읽는 함수이다.
f = open("input.txt", "r", encoding="UTF-8")
count = 0
while count < 3:
    data = f.readline()
    count = count + 1
    print("%d번째 줄: %s" %(count, data), end='')
f.close()

print()
# readlines(): 전체 내용을 한번에 리스트에 담는 함수이다.
f = open("input.txt", "r", encoding="UTF-8")
list = f.readlines()
for i, data in enumerate(list):
    print("%d번째 줄: %s" %(i + 1, data), end='')
print(list)
f.close()

# with: file open, close 다 줄여줌.
with open("input.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
        print("%d번째 줄: %s" %(i + 1, data), end='')


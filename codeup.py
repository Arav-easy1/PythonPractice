# 1036 문자를 아스키코드 값으로 변환 ord()
    # answer = ord(input())
    # print(answer)
# 1037 아스키코드 값을 문자로 출력 chr()
    # answer = int(input())
    # print(chr(answer))
# 1038 두 정수의 합을 출력
    # answer = input().split()
    # add = lambda a, b: int(a) + int(b)
    # print(add(answer[0], answer[1]))
# 1040 정수의 부호를 바꿔서 출력
    # answer = int(input())
    # print(-answer)
# 1048 a에 2의 b제곱 만큼을 곱한 값 출력
    # answer = input().split()
    # result = int(answer[0]) * (2 ** int(answer[1]))
    # print(result)
# 1060 두 정수를 비트단위로 and 하여 출력
    # answer = input().split()
    # for i, k in enumerate(answer):
    #     answer[i] = bin(int(k))[2:].zfill(31)
    # list1 = list(answer[0])
    # list2 = list(answer[1])
    # def and_chenk(a, b):
    #     if a == '1' and b == '1':
    #         return '1'
    #     else:
    #         return '0'
    # answer = list(map(and_chenk, list1, list2))
    # print(int("".join(answer), 2))

# 1061 두 정수를 비트단위로 or 연산하여 출력
    # answer = input().split()
    # for i, k in enumerate(answer):
    #     answer[i] = bin(int(k))[2:].zfill(31)
    # list1 = list(answer[0])
    # list2 = list(answer[1])
    # def and_chenk(a, b):
    #     if a == '1' or b == '1':
    #         return '1'
    #     else:
    #         return '0'
    # answer = list(map(and_chenk, list1, list2))
    # print(int("".join(answer), 2))

# 1062 두 정수를 비트단위로 xor 연산하여 출력
    # answer = input().split()
    # for i, k in enumerate(answer):
    #     answer[i] = bin(int(k))[2:].zfill(31)
    # list1 = list(answer[0])
    # list2 = list(answer[1])
    # def and_chenk(a, b):
    #     if a != b:
    #         return '1'
    #     else:
    #         return '0'
    # answer = list(map(and_chenk, list1, list2))
    # print(int("".join(answer), 2))
# 1064 삼항연산자로 정수 3개 중 제일 작은 수 출력
    # answer = input().split()
    # num1 = int(answer[0])
    # num2 = int(answer[1])
    # num3 = int(answer[2])
    # result = num1 if num1 < num2 and num1 < num3 else (num2 if num2 < num1 and num2 < num3 else num3)
    # print(result)

answer = int(input())
if answer <= 100 and answer >= 90:
    print("A")
elif answer < 90 and answer >= 70:
    print("B")
elif answer < 70 and answer >= 40:
    print("C")
elif answer < 40 and answer >= 0:
    print("D")
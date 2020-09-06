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
# 1076 영문자 1개 입력되고, 그 문자까지의 알파벳 순서대로 출력하기
    # answer = ord(input())
    # a = ord('a')
    # for i in range(a, answer + 1):
    #     print(chr(i))
# 1082 16진수 구구단
    # ip = input()
    # answer = int(ip, 16)
    # for i in range(1, 16):
    #     print("%s*%X=%X" %(ip, i, (answer * i)))
# 1093 출석번호 부른 횟수, 부른 번호 순서로 입력값이 들어왔을때, 각 번호별로 출석 불린 횟수 출력
    # my_list = []
    # for i in range(0, 23):
    #     my_list.append(0)
    # answer = int(input())
    # call_list = input().split()
    # for i in call_list:
    #     my_list[int(i)-1] += 1
    # call_list = list(map(str, my_list))
    # print(" ".join(call_list))
# 1099 개미가 먹이를 찾아 지나가는 길 표시 (2차원 배열)

    # pan = []
    # for i in range(0, 10):
    #     pan.append([])
    #     for j in range(0, 10):
    #         pan[i].append("0")
    #
    # for i in range(0, len(pan)):
    #     pan[i] = input().split()
    #
    #     pan_x = 1
    #     pan_y = 1
    # while 1:
    #     if pan[pan_x][pan_y] == '2':
    #         pan[pan_x][pan_y] = '9'
    #         break
    #     else:
    #         pan[pan_x][pan_y] = '9'
    #         if pan[pan_x][pan_y + 1] == '1':    # 오른쪽 막힘
    #             if pan[pan_x + 1][pan_y] == '1':    # 아래도 막힘
    #                 break
    #             pan_x += 1
    #         else:
    #             pan_y += 1
    #
    # for i in range(0, len(pan)):
    #     print(" ".join(pan[i]))

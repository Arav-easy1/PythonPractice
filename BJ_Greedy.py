# 2839 설탕배달
    # n = int(input())
    # min_pack = n
    # for i in range(0, n//5 +1):
    #     sugar = n
    #     sugar = sugar - (i * 5)
    #     if sugar % 3 == 0:
    #         count = sugar // 3
    #         if min_pack > count + i:
    #             min_pack = count + i
    # if min_pack == n:
    #     print(-1)
    # else:
    #     print(min_pack)
# 11399 ATM
    # count = int(input())
    # atm = list(map(int, input().split()))
    # atm.sort()
    # sum = 0
    # for i in range(0, count):
    #     for j in range(0, i + 1):
    #         sum += atm[j]
    # print(sum)
# 11047 동전 0
    # coin_input = input().split()
    # count = int(coin_input[0])
    # won = int(coin_input[1])
    # coin_list = []
    # for i in range(0, count):
    #     coin_list.append(int(input()))
    # coin_list = coin_list[::-1]
    # coin = 0
    # for i in coin_list:
    #     if won >= i:
    #         zero = won // i
    #         coin += zero
    #         won = won - (zero * i)
    # print(coin)
# 1931 회의실 배정
    # 일단 패스
# 5585 거스름돈
    # won = []
    # coin = 500
    # sw = 0
    # for i in range(0, 6):
    #     won.append(coin)
    #     if sw == 0:
    #         coin //= 5
    #         sw = 1
    #     else:
    #         coin //= 2
    #         sw = 0
    # pay = 1000 - int(input())
    # count = 0
    # for i in won:
    #     coin = i
    #     count += pay // coin
    #     pay = pay % coin
    # print(count)
# 19153 로프
    # n = int(input())
    # rope = []
    # for i in range(0, n):
    #     rope.append(int(input()))
    # rope.sort()
    # answer = []
    # count = len(rope)
    # for i in range(0, len(rope)):
    #     answer.append(rope[i] * count)
    #     count -= 1
    # print(max(answer))
# 15072 잃어버린 괄호
num = input().split('-')
n_sum = 0
first = int(num[0])
num.pop(0)
for i in num:
    if "+" in i:
        plus = i.split("+")
        plus = list(map(int, plus))
        n_sum -= sum(plus)
    else:
        n_sum -= int(i)
print(n_sum + first)

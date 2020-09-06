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

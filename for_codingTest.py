# 복잡도(Complexity)
# 코딩테스트 문제에서 보이는 '시간제한 1초, 메모리 제한 128 MB' 와 같은 문장은 시간 복잡도와 공간 복잡도를 함께 제한하는 것.

# 시간 복잡도(Time Complexity)
# N의 범위가 500인 경우: 시간 복잡도가 O(N^3)인 알고리즘을 설계하면 문제를 풀 수 있다.
# N의 범위가 2,000인 경우: 시간 복잡도가 O(N^2)인 알고리즘을 설계하면 문제를 풀 수 있다.
# N의 범위가 100,000인 경우: 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 풀 수 있다.
# N의 범위가 10,000,000인 경우: 시간 복잡도가 O(N)인 알고리즘을 설계하면 문제를 풀 수 있다.

# # 수행시간 측정 코드
import time
start_time = time.time()    # 측정 시작

# 프로그램 소스 코드
# end_time = time.time()      # 측정 종료
# print("time: ", end_time - start_time)  # 수행 시간 출력

# p92 실전문제 큰 수의 법칙
    # n, m, k = map(int, input().split())
    # numbers = list(map(int, input().split()))
    # numbers.sort(reverse=True)
    # one = numbers[0]
    # two = numbers[1]
    # sum_num = 0
    # count = 0
    # for i in range(m):
    #     if count == k:
    #         sum_num += two
    #         count = 0
    #     else:
    #         sum_num += one
    #         count += 1
    # print(sum_num)

# 좀 더 simple
    # n, m, k = map(int, input().split())
    # numbers = list(map(int, input().split()))
    # numbers.sort(reverse=True)
    # one = numbers[0]
    # two = numbers[1]
    # count = (m // (k + 1) * k) + m % (k + 1)
    # result = 0
    # result = one * count
    # result += two * (m - count)
    # print(result)

# p96 숫자 카드 게임
    # r, c = map(int, input().split())
    # num = 0
    # for i in range(r):
    #     cards = list(map(int, input().split()))
    #     num = max(num, min(cards))
    # print(num)

# p99 1이 될 때까지
    # n, m = map(int, input().split())
    # count = 0
    # for i in range(n):
    #     if n == 1:
    #         break
    #     if n % m == 0:
    #         n //= m
    #     else:
    #         n -= 1
    #     count += 1
    # print(count)
    # time:  5.044707536697388

    # n, m = map(int, input().split())
    # count = 0
    # while True:
    #     temp = (n // m) * m
    #     count += n - temp
    #     n = temp
    #     if n < m:
    #         break
    #     n = n // m
    #     count += 1
    #
    # count += n - 1
    # print(count)
    # time:  2.6595821380615234

# p110 상하좌우
n = int(input())
r = 1
c = 1
route = input().split()
for i in route:
    if i == 'L':
        if c != 1:
            c -= 1
        else:
            continue
    elif i == 'R':
        if c != n:
            c += 1
        else:
            continue
    elif i == 'U':
        if r != 1:
            r -= 1
        else:
            continue
    else:
        if r != n:
            r += 1
        else:
            continue
print(r, c)

end_time = time.time()      # 측정 종료
print("time: ", end_time - start_time)  # 수행 시간 출력

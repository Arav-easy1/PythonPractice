# 복잡도(Complexity)
# 코딩테스트 문제에서 보이는 '시간제한 1초, 메모리 제한 128 MB' 와 같은 문장은 시간 복잡도와 공간 복잡도를 함께 제한하는 것.

# 시간 복잡도(Time Complexity)
# N의 범위가 500인 경우: 시간 복잡도가 O(N^3)인 알고리즘을 설계하면 문제를 풀 수 있다.
# N의 범위가 2,000인 경우: 시간 복잡도가 O(N^2)인 알고리즘을 설계하면 문제를 풀 수 있다.
# N의 범위가 100,000인 경우: 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 풀 수 있다.
# N의 범위가 10,000,000인 경우: 시간 복잡도가 O(N)인 알고리즘을 설계하면 문제를 풀 수 있다.

# # 수행시간 측정 코드
# import time
# start_time = time.time()    # 측정 시작

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
    # n = int(input())
    # r = 1
    # c = 1
    # route = input().split()
    # for i in route:
    #     if i == 'L':
    #         if c != 1:
    #             c -= 1
    #         else:
    #             continue
    #     elif i == 'R':
    #         if c != n:
    #             c += 1
    #         else:
    #             continue
    #     elif i == 'U':
    #         if r != 1:
    #             r -= 1
    #         else:
    #             continue
    #     else:
    #         if r != n:
    #             r += 1
    #         else:
    #             continue
    # print(r, c)

    # n = int(input())
    # x, y = 1, 1
    # plans = input().split()
    #
    # dx = [0, 0, -1, 1]
    # dy = [-1, 1, 0, 0]
    # menual = ['L', 'R', 'U', 'D']
    # for plan in plans:
    #     for i in range(len(menual)):
    #         if plan == menual[i]:
    #             nx = x + dx[i]
    #             ny = y + dy[i]
    #
    #     if nx < 1 or ny < 1 or nx > n or ny > n:
    #         continue
    #     x, y = nx, ny
    #
    # print(x, y)

# p113 시각
    # n = int(input())
    # count = 0
    # h, m, s = 0, 0, 0
    # for hour in range(n+1):
    #     for minute in range(60):
    #         for second in range(60):
    #             if '3' in str(hour) + str(minute) + str(second):
    #                 count += 1
    #
    # print(count)

# p115 왕실의 나이트
    # data = input()
    # r = int(data[1])
    # c = ord(data[0]) - ord('a') + 1
    # move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
    # count = 0
    #
    # for i in move:
    #     nr = r + i[0]
    #     nc = c + i[1]
    #     if nr > 8 or nc > 8 or nr < 1 or nc < 1:    # 혹은 if nr >= 1 and 처럼 안에 들어오면 카운트 늘이기.
    #         continue
    #     count += 1
    #
    # print(count)

# p118 게임 개발
    # n, m = map(int, input().split())
    # game_map = [[0] * m for _ in range(n)]
    # x, y, direction = map(int, input().split())
    # game_map[x][y] = 1
    #
    # array = []
    # for i in range(4):
    #     array.append(list(map(int, input().split())))
    #
    # print(array)
    #
    # dx = [-1, 0, 1, 0]
    # dy = [0, 1, 0, -1]
    #
    # def turn_left():
    #     global direction
    #     direction -= 1
    #     if direction == -1:
    #         direction = 3
    #
    # count = 1
    # turn = 0
    # while True:
    #     turn_left()
    #     nx = x + dx[direction]
    #     ny = y + dy[direction]
    #     if game_map[nx][ny] == 0 and array[nx][ny] == 0:
    #         game_map[nx][ny] = 1
    #         x, y = nx, ny
    #         count += 1
    #         turn = 0
    #     else:
    #         turn += 1
    #     if turn == 4:
    #         nx = x - dx[direction]
    #         ny = y - dy[direction]
    #         if array[nx][ny] == 0:
    #             x, y = nx, ny
    #         else:
    #             break
    #         turn = 0
    # print(count)

# Stack - 스택은 파이썬에서 기본 라이브러리로 사용할 수 있다.
    # stack = []
    # stack.append(5)
    # stack.append(2)
    # stack.append(3)
    # stack.append(7)
    # stack.pop()
    # stack.append(1)
    # stack.append(4)
    # stack.pop()
    # print(stack)
    # print(stack[::-1])

# Queue = 큐 는 deque 라이브러리를 사용해야한다.
    # from collections import deque
    # queue = deque()
    # queue.append(5)
    # queue.append(2)
    # queue.append(3)
    # queue.append(7)
    # queue.popleft()
    # queue.append(1)
    # queue.append(4)
    # queue.popleft()
    # print(queue)

# 재귀 함수
    # def recursive_function(i):
    #     if i == 100:
    #         return
    #     print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다')
    #     recursive_function(i + 1)
    #     print(i, '번째 재귀함수를 종료합니다.')
    #
    # recursive_function(1)

# factorial
    # # iterative(반복적으로)
    # def iterative_fact(n):
    #     result = 1
    #     for i in range(1, n + 1):
    #         result *= i
    #     return result
    #
    # # recursive(재귀적으로)
    # def recursive_fact(n):
    #     if n <= 1:
    #         return 1
    #     return n * recursive_fact(n - 1)
    #
    # print('iterative:', iterative_fact(5))
    # print('recursive:', recursive_fact(5))

# 인접 행렬
    # INF = 999999999     # 무한의 비용 선언
    #
    # graph = [
    #     [0, 7, 5],
    #     [7, 0, INF],
    #     [5, INF, 0]
    # ]
    #
    # print(graph)

# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
    # graph = [[] for _ in range(3)]
    # graph[0].append((1, 7))
    # graph[0].append((2, 5))
    # graph[1].append((0, 7))
    # graph[2].append((0, 5))
    # print(graph)

# DFS(Depth-First Search) 예제
    # def dfs(graph, v, visited):
    #     visited[v] = True
    #     print(v, end=' ')
    #     for i in graph[v]:
    #         if not visited[i]:
    #             dfs(graph, i, visited)
    # graph = [
    #     [],
    #     [2, 3, 8],
    #     [1, 7],
    #     [1, 4, 5],
    #     [3, 5],
    #     [3, 4],
    #     [7],
    #     [2, 6, 8],
    #     [1, 7]
    # ]
    # visited = [False] * 9
    # dfs(graph, 1, visited)

# BFS(Breath First Search) 예제
    # from collections import deque
    # def bfs(graph, start, visited):
    #     queue = deque([start])
    #     visited[start] = True
    #     while queue:
    #         v = queue.popleft()
    #         print(v, end=' ')
    #         for i in graph[v]:
    #             if not visited[i]:
    #                 queue.append(i)
    #                 visited[i] = True
    # graph = [
    #     [],
    #     [2, 3, 8],
    #     [1, 7],
    #     [1, 4, 5],
    #     [3, 5],
    #     [3, 4],
    #     [7],
    #     [2, 6, 8],
    #     [1, 7]
    # ]
    # visited = [False] * 9
    # bfs(graph, 1, visited)

# p149 음료수 얼려 먹기
    # n, m = map(int, input().split())
    #
    # graph = []
    # for i in range(n):
    #     graph.append(list(map(int, input())))
    #
    # def dfs(x, y):
    #     if x <= -1 or y <= -1 or x >= n or y >= m:
    #         return False
    #     if graph[x][y] == 0:
    #         graph[x][y] = 1
    #         dfs(x - 1, y)
    #         dfs(x + 1, y)
    #         dfs(x, y - 1)
    #         dfs(x, y + 1)
    #         return True
    #     return False
    #
    # result = 0
    # for i in range(n):
    #     for j in range(m):
    #         if dfs(i, j) == True:
    #             result += 1
    #
    # print(result)

# p152 미로 탈출
    # from collections import deque
    #
    # n, m = map(int, input().split())
    #
    # graph = []
    # for i in range(n):
    #     graph.append(list(map(int, input())))
    #
    # dx = [-1, 1, 0, 0]
    # dy = [0, 0, -1, 1]
    #
    # def bfs(x, y):
    #     queue = deque()
    #     queue.append((x, y))
    #
    #     while queue:
    #         x, y = queue.popleft()
    #         for i in range(4):
    #             nx = x + dx[i]
    #             ny = y + dy[i]
    #             if nx < 0 or ny < 0 or nx >= n or ny >= m:
    #                 continue
    #             if graph[nx][ny] == 0:
    #                 continue
    #             if graph[nx][ny] == 1:
    #                 graph[nx][ny] = graph[x][y] + 1
    #                 queue.append((nx, ny))
    #     return graph[n - 1][m - 1]
    #
    # print(bfs(0, 0))

# p178 위에서 아래로
    # n = int(input())
    # result = []
    # for i in range(n):
    #     result.append(int(input()))
    # result.sort(reverse=True)
    #
    # for i in result:
    #     print(i, end=" ")

# p180 성적이 낮은 순서로 학생 출력하기
    # n = int(input())
    # array = []
    # for i in range(n):
    #     data = input().split()
    #     array.append((data[0], int(data[1])))
    #
    # array = sorted(array, key=lambda s: s[1])
    #
    # for i in array:
    #     print(i[0], end=" ")

# p182 두 배열의 원소 교체
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    #
    # a.sort()
    # b.sort(reverse=True)
    #
    # for i in range(k):
    #     if a[i] < b[i]:
    #         a[i], b[i] = b[i], a[i]
    #     else:
    #         break
    # print(sum(a))

# 입력 데이터가 많은 문제는 sys 라이브러리를 사용하는 것이 좋다.
    # import sys
    # input_data = sys.stdin.readline().rstrip()
    # print(input_data)

# p197 부품 찾기
    # n = int(input())
    # parts = list(map(int, input().split()))
    # parts.sort()
    # m = int(input())
    # order = list(map(int, input().split()))
    # def bs(array, target, start, end):
    #     if start > end:
    #         return None
    #     mid = (start + end) // 2
    #     if array[mid] == target:
    #         return mid
    #     elif array[mid] < target:
    #         return bs(array, target, mid + 1, end)
    #     else:
    #         return bs(array, target, start, mid - 1)
    # for i in order:
    #     yesOrNo = bs(parts, i, 0, n - 1)
    #     if yesOrNo != None:
    #         print('yes', end=" ")
    #     else:
    #         print("no", end=" ")

# p201 떡볶이 떡 만들기
    # n, m = map(int, input().split())
    # ddeoks = list(map(int, input().split()))
    #
    # start = 0
    # end = max(ddeoks)
    #
    # result = 0
    # while start <= end:
    #     total = 0
    #     mid = (start + end) // 2
    #     for i in ddeoks:
    #         if i > mid:
    #             total += i - mid
    #     if total < m:
    #         end = mid - 1
    #     else:
    #         result = mid
    #         start = mid + 1
    # print(result)

import time
start_time = time.time()    # 측정 시작
# 피보나치
    # def fibo(x):
    #     if x == 1 or x == 2:
    #         return 1
    #     return fibo(x - 1) + fibo(x - 2)
    # print(fibo(35))
    # time:  3.6414012908935547

# 다이나믹 프로그래밍 : 탑다운
    # d = [0] * 100
    # def fibo(x):
    #     if x == 1 or x == 2:
    #         return 1
    #     if d[x] != 0:
    #         return d[x]
    #     d[x] = fibo(x - 1) + fibo(x - 2)
    #     return d[x]
    # print(fibo(99))

# p217 1로 만들기
    # x = int(input())
    #
    # d = [0] * 30001
    #
    # for i in range(2, x + 1):
    #     d[i] = d[i - 1] + 1
    #     if i % 2 == 0:
    #         d[i] = min(d[i], d[i // 2] + 1)
    #     if i % 3 == 0:
    #         d[i] = min(d[i], d[i // 3] + 1)
    #     if i % 5 == 0:
    #         d[i] = min(d[i], d[i // 5] + 1)
    # print(d[x])


end_time = time.time()      # 측정 종료
print("time: ", end_time - start_time)  # 수행 시간 출력


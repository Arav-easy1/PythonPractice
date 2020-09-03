# 문자열 자료형 뒤집기: 슬라이싱 활용
    # str = "Hello World"
    # print(str[::-1])
# len(): 문자열의 길이를 출력
    # str = "Hello World"
    # print(len(str))
# isalpha(): 특정한 문자열이 문자로만 이루어져 있는지 확인(공백x 숫자x)
    # str = "Hello world"
    # print(str.isalpha())    # 공백이 있어서 False임
# isdigit(): 특정한 문자열이 숫자로만 이루어져 있는지 확인(공백x, 문자x)
    # str = "12354"
    # print(str.isdigit())
# isalnum(): 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인(공백x, 특수문자x)
    # str = 'asd1234'
    # print(str.isalnum())
# join(리스트 자료형): 여러 개의 문자열을 구분자와 함께 합치는 함수
    # list = ["hello", 'world', '홍길동']
    # print('_'.join(list))
#sorted(문자열 자료형): 각 문자를 정렬하는 함수
    # str = "helloworld"
    # list = sorted(str)
    # print(list)
    # print(''.join(list))
    # list = sorted(str, reverse=True)
    # print(''.join(list))
# split(토큰): 문자열을 토큰에 따라서 분리하는 함수
    # str = "I wanna watch a movie."
    # list = str.split(' ')
    # print(list)
# fint(서브 문자열): 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
    # str = "I like like you."
    # print(str.find('like')) # 문자 2번째 인덱스에 like가 시작되므로 2가 출력됨.
    # print(str.find('like', 5))  # 5번째 인덱스 뒤에 있는 like를 찾아줘. 7 출력됨.
# upper(), lower(): 문자열을 대문자로 혹은 소문자로 변환해주는 함수
    # str = "Hello World"
    # print(str.upper())
    # print(str.lower())
# strip(): 좌우로 특정한 문자열을 제거하는 함수
    # str = " Hello World tt"
    # print(str.strip())  # 기본적으로 매개변수에 아무것도 안넣으면 자동으로 공백제거
    # print(str.lstrip()) # l이 앞에 붙으면 왼쪽만 제거
    # print(str.rstrip()) # r이 앞에 붙으면 오른쪽만 제거
    # print(str.strip('t'))
# eval(): 문자열 수식 계산해주는 함수
    # exp = "(203+705)*3-(30/6)"
    # print(eval(exp))
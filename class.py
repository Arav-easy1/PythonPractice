# 클래스(Class): 반복되는 불필요한 소스코드를 최소화하면서 현실세계의 사물을 컴퓨터 프로그래밍 상에서 쉽게 표현할 수 있도록 해주는
#               프로그래밍 기술
# 인스턴스: 클래스로 정의된 객체를 프로그램 상에서 이용할 수 있게 만든 변수

# 클래스의 멤버: 클래스 내부에 포함되는 변수
# 클래스의 함수: 클래스 내부에 포함되는 함수. 메소드라고 부름.

# 상속: 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
# 부모와 자식 관계가 존재한다
# 자식 클래스: 부모 클래스를 상속 받은 클래스
class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name, "이(가) 공격을 수행합니다. [전투력: ", self.power, "]")

class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
    def show_info(self):
        print("몬스터 이름: ", self.name, "/ 몬스터 종류: ", self.type)
monster = Monster("슬라임", 10, "초급")
monster.attack()
monster.show_info()